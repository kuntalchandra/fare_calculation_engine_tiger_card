from tiger_card.entities.ticket_cost import TicketCost
from tiger_card.entities.zone import Zone

"""
zones = [1, 2]
costs = {1: [30, 25], 2: [25, 20]}
caps = {1: [100, 500], 2: [80, 400]}
neighbors = {1: [2], 2: [1]}
neighbors_cost = {1: [[35, 30]], 2: [[35, 30]]}
neighbors_cap = {1: [120, 600], 2: [120, 600]}
"""


class ZoneBuilder:
    @staticmethod
    def builder():
        # zone 1
        zone_one = Zone(1)
        zone_one.cost = TicketCost(peak_hour_cost=30, off_peak_hour_cost=25)
        zone_one.daily_cap = 100
        zone_one.weekly_cap = 500
        # direction - zone one to its neighbor
        zone_one_neighbor = Zone(2)
        zone_one_neighbor.cost = TicketCost(peak_hour_cost=35, off_peak_hour_cost=30)
        zone_one_neighbor.daily_cap = 120
        zone_one_neighbor.weekly_cap = 600
        zone_one.neighbors = [zone_one_neighbor]

        # zone 2
        zone_two = Zone(2)
        zone_two.cost = TicketCost(peak_hour_cost=25, off_peak_hour_cost=20)
        zone_two.daily_cap = 80
        zone_two.weekly_cap = 400
        zone_two_neighbor = Zone(1)
        zone_two_neighbor.cost = TicketCost(peak_hour_cost=35, off_peak_hour_cost=30)
        zone_two_neighbor.daily_cap = 120
        zone_two_neighbor.weekly_cap = 600
        zone_two.neighbors = [zone_two_neighbor]
