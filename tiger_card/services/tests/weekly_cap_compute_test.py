from collections import deque
from unittest import TestCase
from tiger_card.data_models.zone_model import ZoneModel
from tiger_card.services.weekly_cap_compute import WeeklyCapComputeService


class WeeklyCapComputeServiceTest(TestCase):
    def setUp(self) -> None:
        self.zones_map = ZoneModel.instance().zones_map()
        self.default_fare = 10
        self.commuting_day = "Monday"

    def test_weekly_cap_not_applicable(self):
        self.assertEqual(self.default_fare,
                         WeeklyCapComputeService.apply_weekly_cap(spent={}, fare=self.default_fare, travel_history={},
                                                                  zones_data=self.zones_map))

    def test_weekly_cap_applicable(self):
        self.assertEqual(0, WeeklyCapComputeService.apply_weekly_cap(spent={self.commuting_day: 600},
                                                                     fare=self.default_fare, travel_history={
                self.commuting_day: deque([["1", "2"]])}, zones_data=self.zones_map))
