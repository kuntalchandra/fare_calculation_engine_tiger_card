from collections import deque
from copy import deepcopy
from typing import Dict, Any


class CapComputeService:
    @staticmethod
    def compute_daily_cap(travel_history: Dict[str, deque], zones_data: Dict[str, Any]) -> int:
        travel_data = deepcopy(travel_history)
        daily_cap = float("inf")
        for commute_day in travel_data:
            travel_q = travel_data[commute_day]
            while travel_q:
                from_zone, to_zone = travel_q.popleft()
                if from_zone == to_zone:  # same zone
                    daily_cap = zones_data[from_zone]["daily_cap"]
                else:  # cross zone travel, higher preference
                    neighbors = zones_data[from_zone]["neighbors"]
                    return neighbors[to_zone]["daily_cap"]
        return daily_cap

    @staticmethod
    def apply_daily_cap(spent: Dict[str, int], commuting_day: str, fare: int, travel_history: Dict[str, deque],
                        zones_data: Dict[str, Any]) -> int:
        if spent[commuting_day] == 0:  # didn't travel earlier today
            return fare
        total_spent = spent[commuting_day]
        daily_cap = CapComputeService.compute_daily_cap(travel_history, zones_data)
        if total_spent + fare > daily_cap:  # exceeded daily cap
            return daily_cap - total_spent
        return fare

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
        weekly_cap = CapComputeService.compute_weekly_cap(travel_history, zones_data)
        if weekly_spent + fare > weekly_cap:  # exceeded weekly cap
            return weekly_cap - weekly_spent
        return fare
