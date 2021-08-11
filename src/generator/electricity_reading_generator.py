from service.time_converter import iso_format_to_unix_time

import math
import random
import datetime


def random_int_between(min_val, max_val):
    return "%02d" % random.randrange(min_val, max_val)


def get_timedelta(sec=60):
    return datetime.timedelta(seconds=sec)


def generate_electricity_readings(num):
    readings = []
    for i in range(num):
        random_time = (datetime.datetime.now() - get_timedelta(i*60)).isoformat()
        random_reading = math.floor(random.random() * 1000)/1000
        readings.append({"time": iso_format_to_unix_time(random_time), "reading": random_reading})

    return readings
