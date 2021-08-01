from collections import defaultdict
from datetime import time
from typing import Dict
from tiger_card.data_models.commute_daytime_model import CommuteDayTimeModel
from tiger_card.data_models.zone_model import ZoneModel
from tiger_card.services.service_exceptions import InvalidZoneException, InvalidDayException, InvalidTimeException


class CommuteComputeService:
    def __init__(self):
        self.zones_map = ZoneModel.instance().zones_map()
        self.days = CommuteDayTimeModel.instance().days_map()
        self.daily_cap = 0
        self.weekly_cap = 0
        self.costs = defaultdict(int)

    def calculate_fare(self, commute_day: str, commute_time: str, from_zone: str, to_zone: str):
        self.validate_input(commute_day, commute_time, from_zone)
        hour, minute = commute_time.split(":")
        commuting_time = time(hour=int(hour), minute=int(minute))

        # default cap
        if not self.daily_cap:
            self.daily_cap = self.zones_map[from_zone]["daily_cap"]
            self.weekly_cap = self.zones_map[from_zone]["weekly_cap"]

        # calculate fare
        if from_zone == to_zone:  # same zone
            zone_data = self.zones_map[from_zone]
        else:  # cross zone
            neighbors = self.zones_map[from_zone]["neighbors"]
            try:
                zone_data = neighbors[to_zone]
            except Exception:
                raise InvalidZoneException("Destination zone is not reachable from {} zone".format(from_zone))
            # travelled cross zone, reset cap limit
            self.daily_cap = zone_data["daily_cap"]
            self.weekly_cap = zone_data["weekly_cap"]

        # cost for this trip
        cost = self.calculate_cost(commuting_time, commute_day, zone_data)
        # finalise the applicable cost
        cost = self.limit_daily_cap_cost(commute_day, cost)
        cost = self.limit_weekly_cap_cost(cost)
        self.costs[commute_day] += cost

        return cost

    def validate_input(self, commute_day: str, commute_time: str, zone: str) -> None:
        if commute_day not in self.days:
            raise InvalidDayException("Invalid commute day {}".format(commute_day))
        try:
            hour, minute = commute_time.split(":")
            time(hour=int(hour), minute=int(minute))
        except Exception:
            raise InvalidTimeException("Invalid commuting hour or minute")
        if zone not in self.zones_map:
            raise InvalidZoneException("Invalid source zone {}".format(zone))

    def calculate_cost(self, commuting_time: time, commute_day: str, zone_data: Dict):
        return zone_data["peak_hour_cost"] if self.is_peak_hour(commuting_time, commute_day) else zone_data[
            "off_peak_hour_cost"]

    def is_peak_hour(self, commuting_time: time, commute_day: str):
        return (self.days[commute_day]["morning_peak_start"] <= commuting_time <= self.days[commute_day]["morning_peak_end"]) or (
                    self.days[commute_day]["evening_peak_start"] <= commuting_time <= self.days[commute_day]["evening_peak_end"])

    def limit_daily_cap_cost(self, commute_day: str, cost: int):
        if self.costs[commute_day] == 0:  # didn't travel earlier today
            return cost
        spent = self.costs[commute_day]
        if spent + cost > self.daily_cap:  # exceeded daily cap
            return self.daily_cap - spent
        return cost

    def limit_weekly_cap_cost(self, cost: int):
        if not self.costs:  # didn't travel earlier this week
            return cost
        weekly_spent = sum([daily_spent for daily_spent in self.costs.values()])
        if weekly_spent + cost > self.weekly_cap:  # exceeded weekly cap
            return self.weekly_cap - weekly_spent
        return cost
