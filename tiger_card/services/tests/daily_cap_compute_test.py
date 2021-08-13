from collections import deque
from unittest import TestCase
from tiger_card.data_models.zone_model import ZoneModel
from tiger_card.services.daily_cap_compute import DailyCapComputeService


class DailyCapComputeServiceTest(TestCase):
    def setUp(self) -> None:
        self.zones_map = ZoneModel.instance().zones_map()
        self.default_fare = 10
        self.commuting_day = "Monday"

    def test_daily_cap_not_applicable(self):
        self.assertEqual(self.default_fare,
                         DailyCapComputeService.apply_daily_cap(spent={}, commuting_day=self.commuting_day,
                                                                fare=self.default_fare, travel_history={},
                                                                zones_data=self.zones_map))

    def test_daily_cap_applicable(self):
        self.assertEqual(0, DailyCapComputeService.apply_daily_cap(spent={self.commuting_day: 120},
                                                                   commuting_day=self.commuting_day,
                                                                   fare=self.default_fare, travel_history={
                self.commuting_day: deque([["1", "2"]])}, zones_data=self.zones_map))

    def test_daily_cap_applicable_different_days(self):
        self.assertEqual(0, DailyCapComputeService.apply_daily_cap(spent={"Monday": 120, "Tuesday": 100},
                                                                   commuting_day="Tuesday",
                                                                   fare=self.default_fare, travel_history={
                "Monday": deque([["1", "2"]]), "Tuesday": deque([["1", "1"]])}, zones_data=self.zones_map))
