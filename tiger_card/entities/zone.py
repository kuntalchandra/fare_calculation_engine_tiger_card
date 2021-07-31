from typing import List

from tiger_card.entities.ticket_cost import TicketCost


class Zone:
    def __init__(self, zone_id: int):
        self._id = zone_id
        self._cost = None
        self._neighbors = None
        self._daily_cap = None
        self._weekly_cap = None

    @property
    def id(self) -> int:
        return self._id

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost: TicketCost):
        self._cost = cost

    @property
    def neighbors(self) -> List[int]:
        return self._neighbors

    @neighbors.setter
    def neighbors(self, neighbors: List):
        self._neighbors = neighbors

    @property
    def daily_cap(self) -> int:
        return self._daily_cap

    @daily_cap.setter
    def daily_cap(self, daily_cap: int) -> None:
        self._daily_cap = daily_cap

    @property
    def weekly_cap(self) -> int:
        return self._weekly_cap

    @weekly_cap.setter
    def weekly_cap(self, weekly_cap: int) -> None:
        self._weekly_cap = weekly_cap
