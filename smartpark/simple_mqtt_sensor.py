""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""

import mqtt_device

class Sensor(mqtt_device.MqttDevice):

    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish('sensor', message)

    def start_sensing(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
        while True:
            print("Press E when 🚗 entered!")
            print("Press X when 🚖 exited!")
            detection = input("E or X> ").upper()
            if detection == 'E':
                self.on_detection("entered")
            else:
                self.on_detection("exited")


if __name__ == '__main__':
    config1 = {'name': 'sensor',
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry'
              }
    # TODO: Read config from file

    sensor1 = Sensor(config1)


    print("Sensor initialized")
    sensor1.start_sensing()

