from collections import defaultdict
from datetime import time
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
        # input validation
        if commute_day not in self.days:
            raise InvalidDayException("Invalid commute day {}".format(commute_day))
        try:
            hour, minute = commute_time.split(":")
            commuting_time = time(hour=int(hour), minute=int(minute))
        except Exception:
            raise InvalidTimeException("Invalid commuting hour or minute")
        if from_zone not in self.zones_map:
            raise InvalidZoneException("Invalid source zone {}".format(from_zone))

        # default cap
        if not self.daily_cap:
            self.daily_cap = self.zones_map[from_zone]["daily_cap"]
            self.weekly_cap = self.zones_map[from_zone]["weekly_cap"]

        # calculate fare
        if from_zone == to_zone:    # same zone
            zone_data = self.zones_map[from_zone]
        else:                       # cross zone
            neighbors = self.zones_map[from_zone]["neighbors"]
            try:
                zone_data = neighbors[to_zone]
            except Exception:
                raise InvalidZoneException("Destination zone is not reachable from {} zone".format(from_zone))
            # travelled cross zone, reset cap limit
            self.daily_cap = zone_data["daily_cap"]
            self.weekly_cap = zone_data["weekly_cap"]

        # cost for this trip
        if self.is_peak_hour(commuting_time, commute_day):
            cost = zone_data["peak_hour_cost"]
        else:
            cost = zone_data["off_peak_hour_cost"]

        # finalise the applicable cost
        if self.costs[commute_day] != 0:    # travelled earlier today
            spent = self.costs[commute_day]
            if spent + cost > self.daily_cap:
                cost = self.daily_cap - spent
        if self.costs:  # travelled earlier this week
            weekly_spent = sum([daily_spent for daily_spent in self.costs.values()])
            if weekly_spent + cost > self.weekly_cap:
                cost = self.weekly_cap - weekly_spent

        self.costs[commute_day] += cost
        return cost

    def is_peak_hour(self, commuting_time: time, commute_day: str):
        return (self.days[commute_day]["morning_peak_start"] <= commuting_time <= self.days[commute_day]["morning_peak_end"]) or (
                    self.days[commute_day]["evening_peak_start"] <= commuting_time <= self.days[commute_day]["evening_peak_end"])

    def is_off_peak_hour(self, commuting_time: time, commute_day: str):
        return (self.days[commute_day]["morning_off_peak_start"] <= commuting_time <= self.days[commute_day]["morning_off_peak_end"]) or (
                    self.days[commute_day]["evening_off_peak_start"] <= commuting_time <= self.days[commute_day]["evening_off_peak_end"])
