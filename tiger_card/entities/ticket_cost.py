class TicketCost:
    def __init__(self, peak_hour_cost: int, off_peak_hour_cost: int):
        self._peak_hour_cost = peak_hour_cost
        self._off_peak_hour_cost = off_peak_hour_cost

    @property
    def peak_hour_cost(self):
        return self._peak_hour_cost

    @property
    def off_peak_hour_cost(self):
        return self._off_peak_hour_cost
