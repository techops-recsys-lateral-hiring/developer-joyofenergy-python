class PricePlan:
    def __init__(self, name, supplier, unit_rate, peak_time_multipliers=[]):
        self.name = name
        self.supplier = supplier
        self.unit_rate = unit_rate
        self.peak_time_multipliers = peak_time_multipliers

    def get_price(self, date_time):
        matching_multipliers = [m for m in self.peak_time_multipliers if m.day_of_week == date_time.isoweekday()]
        return self.unit_rate * matching_multipliers[0].multiplier if len(matching_multipliers) else self.unit_rate

    class DayOfWeek:
        SUNDAY = 0
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THUESDAY = 4
        FRIDAY = 5
        SATURDAY = 6

    class PeakTimeMultiplier:
        def __init__(self, day_of_week, multiplier):
            self.day_of_week = day_of_week
            self.multiplier = multiplier
