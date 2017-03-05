
from enum import Enum, unique

class CellStError(Exception):
    pass

@unique
class CellStatus(Enum):
    empty = 0
    ship = 1
    wound = 2


class Cell:

    def __init__(self, x, y):
        self._y = y
        self._x = x
        self._status = CellStatus.empty

        self.build_mod_vertical = None
        self.build_mod_horizontal = None


    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, v):
        if v in CellStatus:
             self._status = v
        else:
            raise CellStError("клетка не может иметь такой статус")

    def __str__(self):
        return "Cell-({},{})".format(self.x, self.y)

    def __repr__(self):
        return "{},{}".format(self.x, self.y)

if __name__ == '__main__':
    c = Cell(0, 0)
    print(c)