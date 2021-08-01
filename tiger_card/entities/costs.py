from abc import ABCMeta, abstractmethod


class Costs(metaclass=ABCMeta):
    @abstractmethod
    def peak_hour_cost(self):
        pass

    @abstractmethod
    def off_peak_hour_cost(self):
        pass
