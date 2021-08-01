from tiger_card.data_models.singleton import Singleton
from tiger_card.entities.daytime_meta import Weekday, Weekend


@Singleton
class CommuteDayTimeModel:
    def __init__(self):
        self.days = {}

    def days_map(self):
        weekday = Weekday()
        weekend = Weekend()
        for day in weekday.days:
            morning_peak_start, morning_peak_end = Weekday.get_morning_peak_hours()
            evening_peak_start, evening_peak_end = Weekday.get_evening_peak_hours()
            morning_off_peak_start, morning_off_peak_end = Weekday.get_morning_off_peak_hours()
            evening_off_peak_start, evening_off_peak_end = Weekday.get_evening_off_peak_hours()
            self.days[day] = {
                "morning_peak_start": morning_peak_start,
                "morning_peak_end": morning_peak_end,
                "evening_peak_start": evening_peak_start,
                "evening_peak_end": evening_peak_end,
                "morning_off_peak_start": morning_off_peak_start,
                "morning_off_peak_end": morning_off_peak_end,
                "evening_off_peak_start": evening_off_peak_start,
                "evening_off_peak_end": evening_off_peak_end,
            }
        for day in weekend.days:
            morning_peak_start, morning_peak_end = Weekend.get_morning_peak_hours()
            evening_peak_start, evening_peak_end = Weekend.get_evening_peak_hours()
            morning_off_peak_start, morning_off_peak_end = Weekend.get_morning_off_peak_hours()
            evening_off_peak_start, evening_off_peak_end = Weekend.get_evening_off_peak_hours()
            self.days[day] = {
                "morning_peak_start": morning_peak_start,
                "morning_peak_end": morning_peak_end,
                "evening_peak_start": evening_peak_start,
                "evening_peak_end": evening_peak_end,
                "morning_off_peak_start": morning_off_peak_start,
                "morning_off_peak_end": morning_off_peak_end,
                "evening_off_peak_start": evening_off_peak_start,
                "evening_off_peak_end": evening_off_peak_end,
            }
        return self.days
