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

        if vector == Ship.Horizontal:
            self._ship.update(set(x for x in range(bow, bow + size)))
        elif vector == Ship.Vertical:
            assert (bow + (size - 1) * 10) < 100
            self._ship.update(set(x for x in range(bow, (bow + size * 10), 10)))

        self._set_around_ship()
        self._set_all()

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
        m = [-1, 1, -10, 10, -11, -9, 9, 11]
        a = set(cell + x for x in m)
        return a

    def _set_around_ship(self):
        a = set()
        for s in self._ship:
            a.update(self._set_around_cell(s))
        a -= self._ship
        self._around.update(set(x for x in a if Ship.Max >= x >= Ship.Min))

    def _set_all(self):
        self._all.update(self.ship.union(self.around))


if __name__ == '__main__':
    ship = Ship(1, 2, Ship.Vertical)
    # print(ship)
    # print(ship.bow)
    # print(len(ship))
    # print(ship.vector)
    opt = ["bow", "vector", "size", "ship", "around", "all"]
    for v in opt:
        print("{} = {}".format(v, getattr(ship, v)))

