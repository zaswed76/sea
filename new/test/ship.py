from collections import Set, Sequence, MutableSet


class Ship(Set):
    Horizontal = "horizontal"
    Vertical = "vertical"
    def __init__(self, bow, size, vector):
        self.vector = vector
        self.size = size
        self.bow = bow
        self.around = set()

        if vector == Ship.Horizontal:
            self._seq = set(x for x in range(bow, bow + size))
        elif vector == Ship.Vertical:
            assert (bow + (size - 1) * 10) < 100
            self._seq = set(x for x in range(bow, (bow + size * 10), 10))

    def __contains__(self, item):
        return item in self._seq

    def __iter__(self):
        return iter(self._seq)

    def __len__(self):
        return len(self._seq)

    def __repr__(self):
        return "{}".format(self._seq)

    def __add__(self, other):
        self._seq.add(other)
        return self._seq

    def _around_cell(self, cell):
        m = [-1, 1, -10, 10, -11, -9, 9, 11]
        a = set(cell + x for x in m)
        return a

    def around_ship(self):
        a = set()
        for s in self._seq:
            a.update(self._around_cell(s))
        a -= self._seq
        return set(x for x in a if 100 > x > -1)





if __name__ == '__main__':
    ship = Ship(1, 2, Ship.Vertical)
    # print(ship)
    # print(ship.bow)
    # print(len(ship))
    # print(ship.vector)
    print(ship.around_ship())
