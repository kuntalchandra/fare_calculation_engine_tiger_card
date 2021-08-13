from tiger_card.exceptions import TigerCardException


class UnreachableZoneException(TigerCardException):
    def __init__(self, msg, **identifiers):
        super().__init__(msg)
        self.identifiers = identifiers
