class Package:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.c = None
        self.c_prime = None

    def set_x(self, x: float):
        self.x = x

    def set_y(self, y: float):
        self.y = y

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x

    def set_c(self, c: float):
        self.y = c

    def get_c(self):
        return self.c

    def set_c_prime(self, c_prime: float):
        self.c_prime = c_prime

    def get_c_prime(self):
        return self.c_prime
