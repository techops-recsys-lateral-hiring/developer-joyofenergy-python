from flask import abort

from repository.electricity_reading_repository import ElectricityReadingRepository

repository = ElectricityReadingRepository()


def store(data):
    repository.store(data['smartMeterId'], data['electricityReadings'])
    return data


def read(smart_meter_id):
    readings = repository.find(smart_meter_id)
    if len(readings) < 1:
        abort(404)
    else:
        return readings
