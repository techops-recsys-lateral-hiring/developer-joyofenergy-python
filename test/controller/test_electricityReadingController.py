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

    def test_successfully_add_the_reading_against_existing_smart_meter_id(self):
        readingJson1 = {
            "smartMeterId": "meter-100",
            "electricityReadings": [
                { "time": 1505825838, "reading": 0.6 },
                { "time": 1505825848, "reading": 0.65 },
            ]
        }

        readingJson2 = {
            "smartMeterId": "meter-100",
            "electricityReadings": [
                { "time": 1605825849, "reading": 0.7 }
            ]
        }

        self.client.post('/readings/store', json=readingJson1)
        self.client.post('/readings/store', json=readingJson2)
        readings = self.client.get('/readings/read/meter-100').get_json()
        self.assertIn({"time": 1505825838, "reading": 0.6 }, readings)
        self.assertIn({"time": 1505825848, "reading": 0.65 }, readings)
        self.assertIn({"time": 1605825849, "reading": 0.7}, readings)