from collections import defaultdict, deque
from datetime import time
from typing import Dict
from tiger_card.data_models.commute_daytime_model import CommuteDayTimeModel
from tiger_card.data_models.zone_model import ZoneModel
from tiger_card.services.daily_cap_compute import DailyCapComputeService
from tiger_card.services.helper.zone_identifier import ZoneIdentifier
from tiger_card.services.service_exceptions import InvalidZoneException, InvalidDayException, InvalidTimeException
from tiger_card.services.weekly_cap_compute import WeeklyCapComputeService


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

        zone_data = ZoneIdentifier.distinguish_zone_data(zones_map=self.zones_map, from_zone=from_zone, to_zone=to_zone)
        self.travelling_metadata[commute_day].append([from_zone, to_zone])  # queue the travelling history
        fare = self.calculate_cost(commuting_time, commute_day, zone_data)  # fare for this trip
        # finalise the applicable caps
        fare = DailyCapComputeService.apply_daily_cap(spent=self.costs, commuting_day=commute_day, fare=fare,
                                                      travel_history=self.travelling_metadata,
                                                      zones_data=self.zones_map)
        fare = WeeklyCapComputeService.apply_weekly_cap(spent=self.costs, fare=fare,
                                                        travel_history=self.travelling_metadata,
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
