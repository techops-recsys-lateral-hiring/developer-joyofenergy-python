from dataclasses import dataclass


@dataclass
class ElectricityReading:
    time: int
    reading: float

    def __init__(self, json):
        self.time = json["time"]
        self.reading = json["reading"]

    def to_json(self):
        return {
            "time": self.time,
            "reading": self.reading,
        }
