from tiger_card.exceptions import TigerCardException


class InvalidZoneException(TigerCardException):
    def __init__(self, msg, **identifiers):
        super().__init__(msg)
        self.identifiers = identifiers


class InvalidDayException(TigerCardException):
    def __init__(self, msg, **identifiers):
        super().__init__(msg)
        self.identifiers = identifiers


class InvalidTimeException(TigerCardException):
    def __init__(self, msg, **identifiers):
        super().__init__(msg)
        self.identifiers = identifiers
