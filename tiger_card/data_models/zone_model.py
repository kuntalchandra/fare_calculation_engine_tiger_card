from tiger_card.entities.daily_cap import DailyCap
from tiger_card.entities.ticket_cost import TicketCost
from tiger_card.entities.weekly_cap import WeeklyCap
from tiger_card.entities.zone import Zone
from tiger_card.data_models.singleton import Singleton

"""
zones = [1, 2]
costs = {1: [30, 25], 2: [25, 20]}
caps = {1: [100, 500], 2: [80, 400]}
neighbors = {1: [2], 2: [1]}
neighbors_cost = {1: [[35, 30]], 2: [[35, 30]]}
neighbors_cap = {1: [120, 600], 2: [120, 600]}
"""


@Singleton
class ZoneModel:
    def __init__(self):
        self.zones = []
        self.zone_map = {}

    def builder(self):
        # zone 1
        zone_one = Zone(zone_id=1)
        zone_one.cost = TicketCost(peak_hour_cost=30, off_peak_hour_cost=25)
        zone_one.daily_cap = DailyCap(cap=100)
        zone_one.weekly_cap = WeeklyCap(cap=500)
        # direction - zone one to its neighbor
        zone_one_neighbor = Zone(zone_id=2)
        zone_one_neighbor.cost = TicketCost(peak_hour_cost=35, off_peak_hour_cost=30)
        zone_one_neighbor.daily_cap = DailyCap(cap=120)
        zone_one_neighbor.weekly_cap = WeeklyCap(cap=600)
        zone_one.neighbors = [zone_one_neighbor]

        # zone 2
        zone_two = Zone(zone_id=2)
        zone_two.cost = TicketCost(peak_hour_cost=25, off_peak_hour_cost=20)
        zone_two.daily_cap = DailyCap(cap=80)
        zone_two.weekly_cap = WeeklyCap(cap=400)
        zone_two_neighbor = Zone(zone_id=1)
        zone_two_neighbor.cost = TicketCost(peak_hour_cost=35, off_peak_hour_cost=30)
        zone_two_neighbor.daily_cap = DailyCap(cap=120)
        zone_two_neighbor.weekly_cap = WeeklyCap(cap=600)
        zone_two.neighbors = [zone_two_neighbor]

        self.zones.extend([zone_one, zone_two])

    def zones_map(self):
        self.builder()
        for zone in self.zones:
            self.zone_map[str(zone.id)] = {
                "peak_hour_cost": zone.cost.peak_hour_cost,
                "off_peak_hour_cost": zone.cost.off_peak_hour_cost,
                "daily_cap": zone.daily_cap.cap,
                "weekly_cap": zone.weekly_cap.cap
            }
            neighbors = {}
            for neighbor in zone.neighbors:
                neighbors[str(neighbor.id)] = {
                    "peak_hour_cost": neighbor.cost.peak_hour_cost,
                    "off_peak_hour_cost": neighbor.cost.off_peak_hour_cost,
                    "daily_cap": neighbor.daily_cap.cap,
                    "weekly_cap": neighbor.weekly_cap.cap
                }
            self.zone_map[str(zone.id)]["neighbors"] = neighbors
        return self.zone_map
