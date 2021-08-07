from collections import defaultdict, deque
from datetime import time
from typing import Dict
from tiger_card.data_models.commute_daytime_model import CommuteDayTimeModel
from tiger_card.data_models.zone_model import ZoneModel
from tiger_card.services.cap_compute import CapComputeService
from tiger_card.services.service_exceptions import InvalidZoneException, InvalidDayException, InvalidTimeException


class CommuteComputeService:
    def __init__(self):
        self.zones_map = ZoneModel.instance().zones_map()
        self.days = CommuteDayTimeModel.instance().days_map()
        self.costs = defaultdict(int)
        self.travelling_metadata = defaultdict(deque)

    def calculate_fare(self, commute_day: str, commute_time: str, from_zone: str, to_zone: str):
        self.validate_input(commute_day, commute_time, from_zone)
        hour, minute = commute_time.split(":")
        commuting_time = time(hour=int(hour), minute=int(minute))

        # find out applicable fare based on same zone travel or cross zone travel
        if from_zone == to_zone:  # same zone
            zone_data = self.zones_map[from_zone]
        else:  # cross zone
            neighbors = self.zones_map[from_zone]["neighbors"]
            try:
                zone_data = neighbors[to_zone]
            except Exception:
                raise InvalidZoneException("Destination zone is not reachable from {} zone".format(from_zone))

        self.travelling_metadata[commute_day].append([from_zone, to_zone])  # queue the travelling history
        fare = self.calculate_cost(commuting_time, commute_day, zone_data)  # fare for this trip
        # finalise the applicable caps
        fare = CapComputeService.apply_daily_cap(spent=self.costs, commuting_day=commute_day, fare=fare,
                                                 travel_history=self.travelling_metadata, zones_data=self.zones_map)
        fare = CapComputeService.apply_weekly_cap(spent=self.costs, fare=fare, travel_history=self.travelling_metadata,
                                                  zones_data=self.zones_map)
        self.costs[commute_day] += fare
        return fare

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
