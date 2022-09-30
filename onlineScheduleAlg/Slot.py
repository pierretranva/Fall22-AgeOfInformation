from tokenize import Double


class Slot:
    def __init__(self, state: int):
        self.download: Double = 0
        self.state = state
        self.z = None
        self.y = 0
        self.d_presum = 0
        self.d_sum = 0

    def set_z(self, value: int):
        self.z = value

    def set_y(self, value: int):
        self.y = value

    def set_state(self, value: int):
        self.state = value

    def set_download(self, value: int):
        self.download = value

    def set_presum(self, value: Double):
        self.d_presum = value

    def set_d_sum(self, value: Double):
        self.d_sum = value

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_state(self):
        return self.state

    def get_download(self):
        return self.download

    def get_presum(self):
        return self.d_presum

    def get_d_sum(self):
        return self.d_sum
