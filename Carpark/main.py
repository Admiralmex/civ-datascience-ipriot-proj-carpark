import time
from parking_lot import ParkingLot
from sensor import Sensor
from display import Display

CONFIG_PATH = "config.toml"

def main():
    parking_lot = ParkingLot(CONFIG_PATH)
    sensor = Sensor(parking_lot.broker_host, parking_lot.broker_port, parking_lot.sensor_topic)
    display = Display()

    parking_lot.connect()
    sensor.connect()

    while True:
        sensor.publish_event("enter", temperature=22.5)
        time.sleep(5)
        sensor.publish_event("exit", temperature=22.5)
        time.sleep(5)

if __name__ == "__main__":
    main()
