from datetime import datetime

class Car:
    def __init__(self, license_plate: str, model: str):
        self.license_plate = license_plate
        self.model = model
        self.entry_time = datetime.now()
        self.exit_time = None

    def mark_exit(self):
        self.exit_time = datetime.now()
