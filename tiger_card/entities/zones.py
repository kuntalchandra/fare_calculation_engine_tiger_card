from abc import ABCMeta, abstractmethod


class Zones(metaclass=ABCMeta):
    @abstractmethod
    def id(self):
        pass
