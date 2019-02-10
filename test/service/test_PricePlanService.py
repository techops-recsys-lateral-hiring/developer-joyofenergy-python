from unittest import TestCase
from unittest.mock import MagicMock

from domain.electricity_reading import ElectricityReading
from domain.price_plan import PricePlan
from repository.electricity_reading_repository import ElectricityReadingRepository
from repository.price_plan_repository import price_plan_repository
from service.price_plan_service import PricePlanService

class TestElectricityReadingService(TestCase):
    electricity_reading_repository = ElectricityReadingRepository()
    price_plan_service = PricePlanService(electricity_reading_repository)

    def tearDown(self):
        price_plan_repository.clear()

    def test_calculate_costs_against_all_price_plans(self):
        price_plan_repository.store([PricePlan('X1', 'XS1', 10, []),
            PricePlan('X2', 'XS2', 2, []),
            PricePlan('X6', 'XS6', 1, [])])

        reading_service_mock = MagicMock(return_value=[
            ElectricityReading({ "time": 1510307115, "reading": 0.5778640126312636 }),
            ElectricityReading({ "time": 1510307125, "reading": 0.19979840426464207 }),
            ElectricityReading({ "time": 1510307135, "reading": 0.22644598149484024 })
        ])
        self.price_plan_service.electricity_reading_service.retrieve_readings_for = reading_service_mock

        spend = self.price_plan_service.get_list_of_spend_against_each_price_plan_for('smart-meter-1001')
        self.assertEqual(spend[0], { 'X6': 60.24650390344476 })
        self.assertEqual(spend[1], { 'X2': 120.49300780688952 })
        self.assertEqual(spend[2], { 'X1': 602.4650390344476 })