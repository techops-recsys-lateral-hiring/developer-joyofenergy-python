from datetime import datetime

class TimeConverter:
    @staticmethod
    def time_elapsed_in_hours(earliest_unix_timestamp, latest_unix_timestamp):
        return (latest_unix_timestamp - earliest_unix_timestamp) / 3600