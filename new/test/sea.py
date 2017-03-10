
from collections import Set, Sequence, MutableSequence, Hashable, Container

class Cell:
    Min = 0
    Max = 10
    Empty = "empty"
    Ship = "ship"
    Wound = "wound"
    Around = "around"
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
        if other.x == self.x and other.y == self.y:
            return True
        else:
            return False

    def __getitem__(self, item):
        return self.coord[item]

    def __repr__(self):
        return "({},{})".format(*self.coord)

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

class Sea(Set):

    def __init__(self):
        self._seq = set(Cell(y, x) for y in range(10) for x in range(10))
        self._allow = self._seq.copy()
        self._occupied = set()

    @property
    def allow(self):
        return self._allow

    @property
    def occupied(self):
        return self._occupied

    def __getitem__(self, item):
        return list(self._seq)[item]

    def __contains__(self, item):
        return item in self._seq

    def __iter__(self):
        return iter(self._seq)

    def __len__(self):
        return len(self._seq)

    def __repr__(self):
        return "{}".format(self._seq)

    def update(self, ship):
        self._occupied.update(ship)
        self._allow.difference_update(ship)



if __name__ == '__main__':

    from new.test.ship import Ship
    sea = Sea()
    print(sea)






    # cell = Cell(7, 3)
    # cell2 = Cell(7, 5)
    # cell.horizontal_allow = cell2
    # print(cell.horizontal_allow)
