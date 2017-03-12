
from collections import Set, Sequence, MutableSequence, Hashable, UserDict
import numpy

class Cell:
    Min = 0
    Max = 10
    Empty = "0"
    Ship = "8"
    Wound = "x"
    Around = "-"
    def __init__(self, y, x):
        assert (y < Cell.Max and x < Cell.Max) and (y >= Cell.Min and x >= Cell.Min)
        self.coord = (y, x)
        self.x = x
        self.y = y
        self.status = Cell.Empty
        self._vertical_allow = Cell.Max - self.y
        self._horizontal_allow = Cell.Max - self.x

    def __hash__(self):
        return hash((self.y, self.x))

    def __eq__(self, other):
        if other[1] == self.x and other[0] == self.y:
            return True
        else:
            return False

    def __getitem__(self, item):
        return self.coord[item]

    def __repr__(self):
        return "Cell-({},{})".format(*self.coord)

    @property
    def vertical_allow(self):
       return 4 if self._vertical_allow >= 4 else self._vertical_allow

    @vertical_allow.setter
    def vertical_allow(self, cell):
        """

        :param v: координата клетки которая посылает сигнал
        """
        self._vertical_allow = cell.y - self.y


    @property
    def horizontal_allow(self):
       return 4 if self._horizontal_allow >= 4 else self._horizontal_allow

    @horizontal_allow.setter
    def horizontal_allow(self, cell):
        self._horizontal_allow = cell.x - self.x

class Sea(UserDict):
    def __init__(self):
        super().__init__()
        self.data.update({(y, x):Cell(y, x) for y in range(10) for x in range(10)})

    def __str__(self):
        lst = [x.status for x in self.data.values()]
        r = numpy.array([lst[i:i+10] for i in range(0,len(lst),10)])
        return str(r)

    def create_ship(self, bow, size, vector):
        y, x = bow
        _ship = {}
        for x in range(x, x + size):
            _ship[(y, x)] = self.data[(y, x)]
            _ship[(y, x)].status = Cell.Ship
        return _ship



if __name__ == '__main__':
    import pprint
    sea = Sea()
    ship = sea.create_ship((0, 0), 2, 1)
    print(sea)







    # cell = Cell(7, 3)
    # cell2 = Cell(7, 5)
    # cell.horizontal_allow = cell2
    # print(cell.horizontal_allow)
