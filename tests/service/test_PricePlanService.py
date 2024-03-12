from unittest import TestCase
from unittest.mock import MagicMock

from src.domain.electricity_reading import ElectricityReading
from src.domain.price_plan import PricePlan
from src.repository.electricity_reading_repository import ElectricityReadingRepository
from src.repository.price_plan_repository import price_plan_repository
from src.service.price_plan_service import PricePlanService
from src.service.time_converter import iso_format_to_unix_time


class TestPricePlanService(TestCase):
    electricity_reading_repository = ElectricityReadingRepository()
    price_plan_service = PricePlanService(electricity_reading_repository)

    def test_calculate_costs_against_all_price_plans(self):
        price_plan_repository.clear()
        price_plan_repository.store(
            [PricePlan("X1", "XS1", 10, []), PricePlan("X2", "XS2", 2, []), PricePlan("X6", "XS6", 1, [])]
        )

        reading_service_mock = MagicMock(
            return_value=[
                ElectricityReading({"time": iso_format_to_unix_time("2017-11-10T09:00:00"), "reading": 0.65}),
                ElectricityReading({"time": iso_format_to_unix_time("2017-11-10T09:30:00"), "reading": 0.35}),
                ElectricityReading({"time": iso_format_to_unix_time("2017-11-10T10:00:00"), "reading": 0.5}),
            ]
        )
        self.price_plan_service.electricity_reading_service.retrieve_readings_for = reading_service_mock

        spend = self.price_plan_service.get_list_of_spend_against_each_price_plan_for("smart-meter-1001")

        self.assertEqual(spend[0], {"X6": 0.5})
        self.assertEqual(spend[1], {"X2": 1})
        self.assertEqual(spend[2], {"X1": 5})
