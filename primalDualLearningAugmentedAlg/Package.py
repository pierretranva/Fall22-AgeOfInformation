class Package:
    def __init__(self, state: int):
        self.download: int = 0
        self.state = state
        self.z = None
        self.y = 0

    def set_z(self, value: int):
        self.z = value

    def set_y(self, value: int):
        self.y = value

    def set_state(self, value: int):
        self.state = value

    def set_download(self, value: int):
        self.download = value

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_state(self):
        return self.state

    def get_download(self):
        return self.download
