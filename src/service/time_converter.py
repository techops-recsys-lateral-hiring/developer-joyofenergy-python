from datetime import datetime


def iso_format_to_unix_time(iso_format_string):
    return __unix_time_of(datetime.fromisoformat(iso_format_string))


def __unix_time_of(dt):
    return int((dt - datetime(1970, 1, 1)).total_seconds())


def time_elapsed_in_hours(earliest_unix_timestamp, latest_unix_timestamp):
    return (latest_unix_timestamp - earliest_unix_timestamp) / 3600
