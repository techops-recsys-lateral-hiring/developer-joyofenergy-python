import dataclasses
from unittest import TestCase

from src.domain.electricity_reading import ElectricityReading
from src.repository.electricity_reading_repository import ElectricityReadingRepository


class TestElectricityReadingRepository(TestCase):
    def setUp(self):
        self.electricity_reading_repository = ElectricityReadingRepository()
        self.electricity_reading_repository.store(
            "smart-meter-0",
            [
                ElectricityReading({"time": 1507375234, "reading": 0.5}),
                ElectricityReading({"time": 1510053634, "reading": 0.75}),
            ],
        )

    def test_have_new_entry_when_new_smart_meter_id_is_given(self):
        readings = self.electricity_reading_repository.find("smart-meter-0")
        self.assertDictEqual({"time": 1507375234, "reading": 0.5}, dataclasses.asdict(readings[0]))
        self.assertDictEqual({"time": 1510053634, "reading": 0.75}, dataclasses.asdict(readings[1]))

    def test_add_usage_data_against_smart_meter_id_if_it_already_exists(self):
        self.electricity_reading_repository.store(
            "smart-meter-0", [ElectricityReading({"time": 1510572000, "reading": 0.32})]
        )
        readings = self.electricity_reading_repository.find("smart-meter-0")
        self.assertEqual(3, len(readings))
        self.assertIn(ElectricityReading({"time": 1507375234, "reading": 0.5}), readings)
        self.assertIn(ElectricityReading({"time": 1510053634, "reading": 0.75}), readings)
        self.assertIn(ElectricityReading({"time": 1510572000, "reading": 0.32}), readings)
