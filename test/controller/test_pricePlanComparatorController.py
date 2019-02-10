from datetime import datetime
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

    def test_recommend_cheapest_price_plans_no_limit_for_meter_usage(self):
        readings = [
            { "time": self.unix_time_of('2020-01-05T10:30:00'), "reading": 35.0 },
            { "time": self.unix_time_of('2020-01-05T11:00:00'), "reading": 3.0 }
        ]

        readingJson = {
            "smartMeterId": "meter-103",
            "electricityReadings": readings
        }

        self.client.post('/readings/store', json=readingJson)
        res = self.client.get('/price-plans/recommend/meter-103')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), [
            { "price-plan-2": 38 },
            { "price-plan-1": 76 },
            { "price-plan-0": 380 }
        ])

    def unix_time_of(self, iso_date):
        dt = datetime.fromisoformat(iso_date)
        return int((dt - datetime(1970,1,1)).total_seconds())