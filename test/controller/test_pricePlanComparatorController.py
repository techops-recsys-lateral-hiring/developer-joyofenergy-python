import unittest

from repository.price_plan_repository import price_plan_repository
from controller.electricity_reading_controller import repository as readings_repository
from app_initializer import initialize_data

from .setup_test_app import app

class TestPricePlanComparatorController(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        initialize_data()

    def tearDown(self):
        price_plan_repository.clear()
        readings_repository.clear()

    def test_get_costs_against_all_price_plans(self):
        res = self.client.get('/price-plans/compare-all/meter-1')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['pricePlanId'], 'price-plan-1')
        self.assertEqual(len(res.get_json()['pricePlanComparisons']), 3)