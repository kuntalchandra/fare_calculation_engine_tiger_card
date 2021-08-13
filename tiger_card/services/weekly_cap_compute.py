from collections import deque
from copy import deepcopy
from typing import Dict, Any


class WeeklyCapComputeService:
    # TODO: DRY- cross zone checking in Daily and Weekly cap
    @staticmethod
    def compute_weekly_cap(travel_history: Dict[str, deque], zones_data: Dict[str, Any]) -> int:
        travel_data = deepcopy(travel_history)
        weekly_cap = float("inf")
        for commute_day in travel_data:
            travel_q = travel_data[commute_day]
            while travel_q:
                from_zone, to_zone = travel_q.popleft()
                if from_zone == to_zone:  # same zone
                    weekly_cap = zones_data[from_zone]["weekly_cap"]
                else:  # cross zone travel, higher preference
                    neighbors = zones_data[from_zone]["neighbors"]
                    return neighbors[to_zone]["weekly_cap"]
        return weekly_cap

    @staticmethod
    def apply_weekly_cap(spent: Dict[str, int], fare: int, travel_history: Dict[str, deque],
                         zones_data: Dict[str, Any]) -> int:
        if not spent:  # didn't travel earlier this week
            return fare
        weekly_spent = sum([daily_spent for daily_spent in spent.values()])
        weekly_cap = WeeklyCapComputeService.compute_weekly_cap(travel_history, zones_data)
        if weekly_spent + fare > weekly_cap:  # exceeded weekly cap
            return weekly_cap - weekly_spent
        return fare
