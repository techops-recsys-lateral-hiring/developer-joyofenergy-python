class ElectricityReadingRepository:
    def __init__(self):
        self.meter_associated_readings = {}

    def store(self, smart_meter_id, readings):
        if smart_meter_id in self.meter_associated_readings:
            existing_list_of_readings = self.meter_associated_readings.get(smart_meter_id)
            self.meter_associated_readings[smart_meter_id] = readings + existing_list_of_readings
        else:
            self.meter_associated_readings[smart_meter_id] = readings

    def find(self, smart_meter_id):
        if smart_meter_id in self.meter_associated_readings:
            return self.meter_associated_readings[smart_meter_id]
        else:
            return []

    def clear(self):
        self.meter_associated_readings = {}
