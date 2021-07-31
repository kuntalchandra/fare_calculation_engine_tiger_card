class TigerCardException(Exception):
    pass


class InvalidCommandException(TigerCardException):
    def __init__(self, msg, **identifiers):
        super().__init__(msg)
        self.identifiers = identifiers
