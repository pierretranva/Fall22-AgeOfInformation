from re import X


class Slot:
    def __init__(self, packages: list):
        self.packages: list = packages
        self.x: float = 0

    def get_packages(self):
        return self.packages

    def set_x(self):
        self.x = X

    def get_x(self):
        return self.x
