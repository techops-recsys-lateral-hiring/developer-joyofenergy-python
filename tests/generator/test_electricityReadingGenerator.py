from datetime import datetime
from unittest import TestCase
from unittest.mock import patch

from src.generator import electricity_reading_generator


class TestElectricityReadingGenerator(TestCase):
    def test_generate_electricity_readings(self):
        generated = electricity_reading_generator.generate_electricity_readings(10)
        self.assertEqual(len(generated), 10)
        for r in generated:
            self.assertEqual(datetime.fromtimestamp(r["time"]).year, datetime.now().year)
            self.assertGreaterEqual(r["reading"], 0)
            self.assertLessEqual(r["reading"], 1)

    def test_return_two_digit_number_for_single_digit_number(self):
        with patch("random.randrange", return_value=9):
            self.assertEqual(electricity_reading_generator.random_int_between(0, 1), "09")

    def test_return_two_digit_number_for_two_digit_number(self):
        with patch("random.randrange", return_value=11):
            self.assertEqual(electricity_reading_generator.random_int_between(0, 1), "11")
