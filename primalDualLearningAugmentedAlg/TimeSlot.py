from re import X
import re
import Package

class TimeSlot:
    def __init__(self, packages: list):
        self.packages: list = packages
        self.x: float = 0

    def get_packages(self) -> list:
        return self.packages
    
    def get_package_at_index(self, index: int) -> Package:
        return self.packages[index]

    def set_x(self):
        self.x = X

    def get_x(self) -> float:
        return self.x
