from datetime import datetime
import math
import random

from domain.electricity_reading import ElectricityReading

def random_int_between(min_val, max_val):
    return "%02d" % random.randrange(min_val, max_val)

def unix_time_of(dt):
    return (dt - datetime(1970, 1, 1)).total_seconds()

def generate_electricity_readings(num):
    readings = []
    for i in range(num):
        random_time = datetime.fromisoformat(f"2001-{random_int_between(1,12)}-{random_int_between(1,28)}T{random_int_between(0,23)}:{random_int_between(0,59)}:{random_int_between(0,59)}")
        random_reading = math.floor(random.random() * 1000)/1000
        readings.append(ElectricityReading({"time": unix_time_of(random_time), "reading": random_reading}))

    return readings