import tomllib
import paho.mqtt.client as mqtt
import json
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

    def connect(self):
        self.client.connect(self.broker_host, self.broker_port)
        self.client.subscribe(self.sensor_topic)
        self.client.on_message = self._on_message
        self.client.loop_start()

    def _on_message(self, client, userdata, msg):
        try:
            message = msg.payload.decode()
            data = json.loads(message)
            event_type = data.get("event")

            print(f"Received MQTT event: {event_type}")

            if event_type == "enter":
                self.enter()
            elif event_type == "exit":
                self.exit()
            else:
                print(f"Unknown event type: {event_type}")
        except Exception as e:
            print(f"Failed to handle message: {e}")

    def enter(self):
        """Handles a car entering. Decreases available spaces and publishes update."""
        if self.available_spaces > 0:
            self.available_spaces -= 1
        self.publish_update()

    def exit(self):
        if self.available_spaces < self.total_spaces:
            self.available_spaces += 1
        self.publish_update()

    def publish_update(self):
        payload = {
            "available_spaces": self.available_spaces,
            "total_spaces": self.total_spaces,
            "timestamp": datetime.now().isoformat()
        }
        self.client.publish(self.carpark_topic, str(payload))
        with open(self.log_file, "a") as f:
            f.write(f"{payload}\n")
