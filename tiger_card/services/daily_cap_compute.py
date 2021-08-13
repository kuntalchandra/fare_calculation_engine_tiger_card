from collections import deque
from copy import deepcopy
from typing import Dict, Any


class DailyCapComputeService:
    # TODO: DRY- cross zone checking in Daily and Weekly cap
    @staticmethod
    def compute_daily_cap(travel_history: deque, zones_data: Dict[str, Any]) -> int:
        travel_data = deepcopy(travel_history)
        while travel_data:
            from_zone, to_zone = travel_data.popleft()
            if from_zone == to_zone:  # same zone
                daily_cap = zones_data[from_zone]["daily_cap"]
            else:  # cross zone travel, higher preference
                neighbors = zones_data[from_zone]["neighbors"]
                return neighbors[to_zone]["daily_cap"]
        return daily_cap

    @staticmethod
    def apply_daily_cap(spent: Dict[str, int], commuting_day: str, fare: int, travel_history: Dict[str, deque],
                        zones_data: Dict[str, Any]) -> int:
        if commuting_day not in spent or spent[commuting_day] == 0:  # didn't travel earlier today
            return fare
        total_spent = spent[commuting_day]
        daily_cap = DailyCapComputeService.compute_daily_cap(travel_history[commuting_day], zones_data)
        if total_spent + fare > daily_cap:  # exceeded daily cap
            return daily_cap - total_spent
        return fare
