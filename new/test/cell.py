

from collections import Sequence

class Cell:
    def __init__(self, y, x):
        self.coord = (y, x)
        self.x = x
        self.y = y

    def __getitem__(self, item):
        return self.coord[item]




if __name__ == '__main__':
    cell = Cell(1, 1)
    print(cell[0])
    print(cell[1])

