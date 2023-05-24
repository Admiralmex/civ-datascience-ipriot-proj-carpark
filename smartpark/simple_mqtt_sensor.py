class Sensor:
    def __init__(self, config):
        self.name = config['name']
        self.location = config['location']
    def start_sensing(self):
        while True:
            reply = input("Is there a car?")
            if reply == 'y':
                print("Car, I saw a car!!")

if __name__ == '__main__':
    config = {'name': 'super sensor',
              'location': 'L306'}
    sensor = Sensor(config)
