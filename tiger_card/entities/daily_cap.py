from tiger_card.entities.caps import Caps


class DailyCap(Caps):
    def __init__(self, cap: int):
        self._cap = cap

    @property
    def cap(self):
        return self._cap
