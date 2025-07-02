import unittest
from parking_lot import ParkingLot

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        self.config_path = "tests/test_config.toml"
        with open(self.config_path, "w") as f:
            f.write("""[parking_lot]
location = "Test"
total_spaces = 2
broker_host = "localhost"
broker_port = 1883
sensor_topic = "sensor"
carpark_topic = "carpark"
log_file = "tests/log.txt"
""")
        self.pl = ParkingLot(self.config_path)

    def test_no_negative_spaces(self):
        self.pl.available_spaces = 0
        self.pl.enter()
        self.assertEqual(self.pl.available_spaces, 0)

    def test_exit_increases_spaces(self):
        self.pl.available_spaces = 1
        self.pl.exit()
        self.assertEqual(self.pl.available_spaces, 2)

if __name__ == "__main__":
    unittest.main()
