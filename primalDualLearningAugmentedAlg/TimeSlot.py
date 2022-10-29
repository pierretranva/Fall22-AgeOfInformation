from re import X
import Package

class TimeSlot:
    def __init__(self, packages: list):
        self.packages: list = packages
        self.x: float = 0

    def get_packages(self) -> list:
        return self.packages

    def set_x(self):
        self.x = X

    def get_x(self) -> float:
        return self.x
