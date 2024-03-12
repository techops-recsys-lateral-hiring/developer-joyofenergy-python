from datetime import datetime
from unittest import TestCase

from src.domain.price_plan import PricePlan


class TestPricePlan(TestCase):
    def test_return_the_base_price_given_an_off_peak_date_time(self):
        peak_time_multiplier = PricePlan.PeakTimeMultiplier(PricePlan.DayOfWeek.WEDNESDAY, 10)
        off_peak_time = datetime(2000, 1, 1, 11, 11, 11)

        plan = PricePlan("plan-name", "supplier-name", 1, [peak_time_multiplier])

        price = plan.get_price(off_peak_time)

        self.assertEqual(price, 1)

    def test_return_a_peak_price_given_a_datetime_matching_peak_day(self):
        peak_time_multiplier = PricePlan.PeakTimeMultiplier(PricePlan.DayOfWeek.WEDNESDAY, 10)
        off_peak_time = datetime(2000, 1, 5, 11, 11, 11)

        plan = PricePlan("plan-name", "supplier-name", 1, [peak_time_multiplier])

        price = plan.get_price(off_peak_time)

        self.assertEqual(price, 10)
