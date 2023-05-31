""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""
import paho.mqtt.client as paho


class Sensor:
    def __init__(self, config, device_name = 'sensor'):
        self.name = config['name']
        self.location = config['location']

        # Define topic components:
        self.topic_root = config['topic-root']
        self.topic_qualifier = config['topic-qualifier']
        self.topic_device = device_name
        self.topic = self._create_topic_string()

        # Configure broker
        self.broker = config['broker']
        self.port = config['port']
        self.type = config['type'] # ENTRY/EXIT
        
        # initialise a paho client and bind it to the object (has-a)

        self.client = paho.Client()
        self.client.connect(self.broker,
                            self.port)

    def _create_topic_string(self):
        return (f"{self.topic_root}/{self.location}/" +
                f"{self.topic_device}/{self.topic_qualifier}")

    def on_detection(self, message):
        """The method that is triggered when a detection occurs"""
        message =f'{self.type}, {message}'
        self.client.publish(self.topic, message)

    def start_sensing(self):
        """a blocking event loop that waits for detection events, in this case Enter presses"""
        while True:
            input("Press Enter when 🚗 detected!")
            self.on_detection("Car detection took place")


if __name__ == '__main__':
    config = {'name': 'super sensor',
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry'
              }

    sensor = Sensor(config)
    print("Sensor initialized")
    sensor.start_sensing()
