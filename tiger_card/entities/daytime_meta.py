from datetime import time


class Weekday:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    @staticmethod
    def get_morning_peak_hours():
        return [time(hour=7), time(hour=10, minute=30)]

    @staticmethod
    def get_evening_peak_hours():
        return [time(hour=17), time(hour=20)]

    @staticmethod
    def get_morning_off_peak_hours():
        return [time(hour=10, minute=31), time(hour=16, minute=59)]

    @staticmethod
    def get_evening_off_peak_hours():
        return [time(hour=20, minute=1), time(hour=6, minute=59)]


class Weekend:
    def __init__(self):
        self.days = ["Saturday", "Sunday"]

    @staticmethod
    def get_morning_peak_hours():
        return [time(hour=9), time(hour=11)]

    @staticmethod
    def get_evening_peak_hours():
        return [time(hour=18), time(hour=22)]

    @staticmethod
    def get_morning_off_peak_hours():
        return [time(hour=11, minute=1), time(hour=17, minute=59)]

    @staticmethod
    def get_evening_off_peak_hours():
        return [time(hour=22, minute=1), time(hour=8, minute=59)]
