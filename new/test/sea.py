
from collections import Set, Sequence, MutableSequence, Hashable, UserDict
import numpy
from new.test.fleet import Fleet



class Cell:
    Min = 0
    Max = 10
    Empty = "0"
    Ship = "8"
    Wound = "X"
    Around = "*"
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

class Ship(UserDict):
    Horizontal = "horizontal"
    Vertical = "vertical"
    def __init__(self, sea, bow, size, vector):
        super().__init__()
        self.sea = sea
        self.ship = self.data
        self.around = {}
        self.all = {}
        y, x = bow
        if vector == Ship.Horizontal:
            self.data.update({(y, x): sea[(y, x)] for x in range(x, x + size)})
        elif vector == Ship.Vertical:
            self.data.update({(y, x): sea[(y, x)] for y in range(y, y + size)})

        self.__mx = [-1, 1, -1, 0, 1, -1, 0, 1]
        self.__my = [0, 0, -1, -1, -1, 1, 1, 1]

        self._set_around_ship()
        self._set_all()
        self._set_status()

    def _set_status(self):
        for k, c in self.all.items():
            if k in self.ship:
                c.status = Cell.Ship
            elif k in self.around:
                c.status = Cell.Around



    def _get_around_cell(self, cell):
        y, x = cell
        a = set(((y + _y), (x + _x)) for _y, _x in zip(self.__my, self.__mx))
        return a

    def _set_around_ship(self):
        for name in self.data:
            around_cell = self._get_around_cell(name)
            for k in around_cell:
                if k in self.sea:
                    if not k in self.ship:
                        self.around[k] = self.sea[k]

    def _set_all(self):
        self.all.update(self.ship)
        self.all.update(self.around)



class Sea(UserDict):
    def __init__(self):
        super().__init__()
        self.data.update({(y, x):Cell(y, x) for y in range(10) for x in range(10)})
        self.fleet = Fleet()

    def __str__(self):
        lst = [x.status for x in self.data.values()]
        r = numpy.array([lst[i:i+10] for i in range(0,len(lst),10)])
        return str(r)

    def create_ship(self, bow, size, vector):
        return Ship(self, bow, size, vector)






if __name__ == '__main__':
    sea = Sea()
    ship = sea.create_ship((5, 5), 4, Ship.Vertical)
    sea.fleet.add_ship(ship)
    x = (5, 5)
    if x in sea.fleet:
        sea[x].status = Cell.Wound
    print(sea)







    # cell = Cell(7, 3)
    # cell2 = Cell(7, 5)
    # cell.horizontal_allow = cell2
    # print(cell.horizontal_allow)
