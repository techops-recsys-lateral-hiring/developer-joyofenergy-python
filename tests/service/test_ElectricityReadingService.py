from unittest import TestCase
from unittest.mock import MagicMock

from src.domain.electricity_reading import ElectricityReading
from src.repository.electricity_reading_repository import ElectricityReadingRepository
from src.service.electricity_reading_service import ElectricityReadingService
from src.service.time_converter import iso_format_to_unix_time


class TestElectricityReadingService(TestCase):
    def setUp(self):
        self.repository = ElectricityReadingRepository()
        self.repository.store = MagicMock()
        self.electricity_reading_service = ElectricityReadingService(self.repository)

    def test_call_repository_to_store_readings(self):
        json = {
            "smartMeterId": "meter-45",
            "electricityReadings": [
                {"time": iso_format_to_unix_time("2015-03-02T08:55:00"), "reading": 0.812},
                {"time": iso_format_to_unix_time("2015-09-02T08:55:00"), "reading": 0.23},
            ],
        }

        self.electricity_reading_service.store_reading(json)

        self.repository.store.assert_called_with(
            "meter-45",
            [
                ElectricityReading({"time": iso_format_to_unix_time("2015-03-02T08:55:00"), "reading": 0.812}),
                ElectricityReading({"time": iso_format_to_unix_time("2015-09-02T08:55:00"), "reading": 0.23}),
            ],
        )
