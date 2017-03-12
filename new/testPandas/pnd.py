

from collections import UserDict



class Ship(UserDict):
    def __init__(self, sea, bow):
        super().__init__()

        self.data[bow] = 5
        self.data[bow+1] = sea[bow+1]


