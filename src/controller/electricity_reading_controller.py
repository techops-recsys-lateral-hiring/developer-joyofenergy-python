from flask import abort

# Data to serve with our API
DEMO = {
    "smartMeterId": 123,
    "electricityReadings": [
        {"time": 234, "reading": 345.6}
    ]
}


def store():
    return DEMO


def read(smart_meter_id):
    readings = [2]
    if len(readings) < 1:
        abort(404)
    else:
        return DEMO
