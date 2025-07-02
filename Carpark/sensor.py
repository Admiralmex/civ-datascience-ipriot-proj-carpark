import paho.mqtt.client as mqtt
import json
from datetime import datetime


class Sensor:
    def __init__(self, broker_host: str, broker_port: int, topic: str):
        self.client = mqtt.Client()
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.topic = topic

    def connect(self):
        self.client.connect(self.broker_host, self.broker_port)
        self.client.loop_start()

    def publish_event(self, event_type: str, temperature: float, license_plate: str, model: str):
        payload = {
            "event": event_type,
            "temperature": temperature,
            "timestamp": datetime.now().isoformat(),
            "license_plate": license_plate,
            "model": model
        }
        print(f"Publishing to MQTT: {payload}")
        self.client.publish(self.topic, json.dumps(payload))
