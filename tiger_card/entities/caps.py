from abc import ABCMeta, abstractmethod


class Caps(metaclass=ABCMeta):
    @abstractmethod
    def cap(self):
        pass
