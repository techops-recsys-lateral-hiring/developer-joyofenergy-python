from service.time_converter import iso_format_to_unix_time

import math
import random


def random_int_between(min_val, max_val):
    return "%02d" % random.randrange(min_val, max_val)


def generate_electricity_readings(num):
    readings = []
    for i in range(num):
        random_time = f"2001-{random_int_between(1,12)}-{random_int_between(1,28)}T{random_int_between(0,23)}:{random_int_between(0,59)}:{random_int_between(0,59)}"
        random_reading = math.floor(random.random() * 1000)/1000
        readings.append({"time": iso_format_to_unix_time(random_time), "reading": random_reading})

    return readings
