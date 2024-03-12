import unittest

from fastapi.testclient import TestClient

from src.controller.electricity_reading_controller import repository as readings_repository
from src.main import app
from src.service.time_converter import iso_format_to_unix_time


class TestPricePlanComparatorController(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_costs_against_all_price_plans(self):
        res = self.client.get("/price-plans/compare-all/smart-meter-1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["pricePlanId"], "price-plan-1")
        self.assertEqual(len(res.json()["pricePlanComparisons"]), 3)

    def test_recommend_cheapest_price_plans_no_limit_for_meter_usage(self):
        readings_repository.clear()

        readings = [
            {"time": iso_format_to_unix_time("2020-01-05T10:30:00"), "reading": 35.0},
            {"time": iso_format_to_unix_time("2020-01-05T11:00:00"), "reading": 5.0},
        ]

        readingJson = {"smartMeterId": "meter-103", "electricityReadings": readings}

        self.client.post("/readings/store", json=readingJson)
        res = self.client.get("/price-plans/recommend/meter-103")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.json(),
            [{"price-plan-2": 40}, {"price-plan-1": 80}, {"price-plan-0": 400}],
        )
