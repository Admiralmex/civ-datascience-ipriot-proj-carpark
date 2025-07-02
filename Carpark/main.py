import time
import random
from parking_lot import ParkingLot
from sensor import Sensor
from display import Display

CONFIG_PATH = "config.toml"
entered_cars = []

def main():
    parking_lot = ParkingLot(CONFIG_PATH)
    sensor = Sensor(parking_lot.broker_host, parking_lot.broker_port, parking_lot.sensor_topic)
    display = Display()

    parking_lot.connect()
    sensor.connect()

    while True:
        # Create a new car
        license_plate = f"MOO-{random.randint(100, 999)}"
        model = random.choice(["Mazda", "Toyota", "Tesla"])

        print(f"\nSimulating ENTER for {license_plate} ({model})")
        sensor.publish_event("enter", 22.5, license_plate, model)
        entered_cars.append((license_plate, model))
        time.sleep(5)

        if entered_cars:
            license_plate, model = entered_cars.pop(0)
            print(f"\nSimulating EXIT for {license_plate} ({model})")
            sensor.publish_event("exit", 22.5, license_plate, model)
        time.sleep(5)

if __name__ == "__main__":
    main()
