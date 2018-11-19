import unittest
import config

app = config.app
app.testing = True
connex_app = config.connex_app
connex_app.add_api('swagger.yml', strict_validation=True)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_successfully_add_the_reading_against_new_smart_meter_id(self):
        readingJson = {
            "smartMeterId": "meter-11",
            "electricityReadings": [
                {"time": 1505825656, "reading": 0.6}
            ]
        }

        response = self.client.post('/readings/store', json=readingJson)
        self.assertEqual(200, response.status_code)
