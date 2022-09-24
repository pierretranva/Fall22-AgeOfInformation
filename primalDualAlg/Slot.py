class Slot:
    def __init__(self, state: int):
        self.download = None
        self.state = state
        self.y = 0
    
    def set_state(self, value: int):
        self.state =value

    def set_download(self, value: int):
        self.download = value

    def set_y(self, value: int):
        self.y =value

    def get_state(self):
        return self.state

    def get_download(self):
        return self.download
           





