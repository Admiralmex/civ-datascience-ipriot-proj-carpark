import tomllib
import paho.mqtt.client as mqtt
import json
from car import Car
from datetime import datetime

class ParkingLot:
    """Manages car entry/exit and updates availability based on MQTT messages."""
    def __init__(self, config_path: str):
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
        pl_cfg = config["parking_lot"]
        self.location = pl_cfg["location"]
        self.total_spaces = pl_cfg["total_spaces"]
        self.available_spaces = self.total_spaces
        self.broker_host = pl_cfg["broker_host"]
        self.broker_port = pl_cfg["broker_port"]
        self.sensor_topic = pl_cfg["sensor_topic"]
        self.carpark_topic = pl_cfg["carpark_topic"]
        self.log_file = pl_cfg["log_file"]
        self.client = mqtt.Client()
        self.bays = {i: {"status": "available", "car": None} for i in range(1, self.total_spaces + 1)}

    def find_available_bay(self):
        for bay_number, data in self.bays.items():
            if data["status"] == "available":
                return bay_number
        return None

    def connect(self):
        self.client.connect(self.broker_host, self.broker_port)
        self.client.subscribe(self.sensor_topic)
        self.client.on_message = self._on_message
        self.client.loop_start()

    def _on_message(self, client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode())
            event = data.get("event")
            license_plate = data.get("license_plate")
            model = data.get("model")

            print(f"Received MQTT event: {event} for {license_plate} ({model})")

            if event == "enter":
                self.enter(license_plate, model)
            elif event == "exit":
                self.exit(license_plate)
        except Exception as e:
            print(f"Failed to handle message: {e}")

    def enter(self, license_plate: str, model: str):
        """Handles a car entering. Decreases available spaces and publishes update."""
        bay_number = self.find_available_bay()
        if bay_number is None:
            print("Carpark full")
            return

        car = Car(license_plate, model)
        self.bays[bay_number]["status"] = "occupied"
        self.bays[bay_number]["car"] = car
        self.available_spaces -= 1
        self.publish_update()

    def exit(self, license_plate: str):
        for bay_number, data in self.bays.items():
            car = data["car"]
            if car and car.license_plate == license_plate:
                car.mark_exit()
                self.bays[bay_number]["status"] = "available"
                self.bays[bay_number]["car"] = None
                self.available_spaces += 1
                self.publish_update()
                return
        print("Car not found")
        self.publish_update()

    def publish_update(self):
        payload = {
            "available_spaces": self.available_spaces,
            "total_spaces": self.total_spaces,
            "timestamp": datetime.now().isoformat()
        }
        print(f"Publishing update: {payload}")
        self.client.publish(self.carpark_topic, json.dumps(payload))
        with open(self.log_file, "a") as f:
            f.write(f"{payload}\n")

        print("Updated bay status:")
        for bay, data in self.bays.items():
            car = data["car"]
            print(f"Bay {bay}: {data['status']} - {car.license_plate if car else 'None'}")

