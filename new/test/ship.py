from collections import Set, Sequence, MutableSet


class Ship(Set):
    Max = 99
    Min = 0
    Horizontal = "horizontal"
    Vertical = "vertical"
    def __init__(self, bow, size, vector):
        self.vector = vector
        self.size = size
        self.bow = bow
        self._ship = set()
        self._around = set()
        self._all = set()
        self.__mx = [-1, 1, -1, 0, 1, -1, 0, 1]
        self.__my = [0, 0, -1, -1, -1, 1, 1, 1]
        if vector == Ship.Horizontal:
            self._ship.update(set((self.y, x) for x in range(self.x, self.x + size)))
        elif vector == Ship.Vertical:
            self._ship.update(set((y, self.x) for y in range(self.y, self.y + size)))
        #
        self._set_around_ship()
        # self._set_all()

    @property
    def x(self):
        return self.bow[0]

    @property
    def y(self):
        return self.bow[1]

    @property
    def ship(self):
        return self._ship

    @property
    def around(self):
        return self._around

    @property
    def all(self):
        return self._all

    def __contains__(self, item):
        return item in self._ship

    def __iter__(self):
        return iter(self._ship)

    def __len__(self):
        return len(self._ship)

    def __repr__(self):
        return "{}".format(self._ship)

    def __add__(self, other):
        self._ship.add(other)
        return self._ship

    def _set_around_cell(self, cell):
        y, x = cell
        return set((y + _y, x + _x) for _y, _x in zip(self.__my, self.__mx))

    def _set_around_ship(self):
        a = set()
        for cell in self._ship:
            a.update(self._set_around_cell(cell))
        a.difference_update(self.ship)
        self._around.update(a)

    def _set_all(self):
        self._all.update(self.ship.union(self.around))


if __name__ == '__main__':
    ship = Ship((1, 1), 1, Ship.Vertical)
    print(ship)
    print(ship.around)
    # print(ship.bow)
    # print(ship.bow)
    # print(len(ship))
    # print(ship.vector)
    # opt = ["bow", "vector", "size", "ship", "around", "all"]
    # for v in opt:
    #     print("{} = {}".format(v, getattr(ship, v)))

