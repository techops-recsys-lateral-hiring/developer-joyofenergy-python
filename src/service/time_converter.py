from datetime import datetime

class TimeConverter:
    @staticmethod
    def time_elapsed_in_hours(earliest_datetime, latest_datetime):
        return (latest_datetime - earliest_datetime).total_seconds() / 3600