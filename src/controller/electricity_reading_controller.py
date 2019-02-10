from flask import abort

from repository.electricity_reading_repository import ElectricityReadingRepository
from service.electricity_reading_service import ElectricityReadingService

repository = ElectricityReadingRepository()
service = ElectricityReadingService(repository)


def store(data):
    service.store_reading(data)
    return data


def read(smart_meter_id):
    readings = service.retrieve_readings_for(smart_meter_id)
    if len(readings) < 1:
        abort(404)
    else:
        return [r.to_json() for r in readings]
