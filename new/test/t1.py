
from collections import Set, Sequence, MutableSet


class Sea(Set):

    def __init__(self, iterable):

        self._seq = lst = set()
        for value in iterable:
            if value not in lst:
                lst.add(value)
        self._allow = self._seq.copy()
        self._occupied = set()

    @property
    def allow(self):
        return self._allow

    @property
    def occupied(self):
        return self._occupied

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

    def update(self, ship):
        self._occupied |= ship
        self._allow -= ship



if __name__ == '__main__':


    sea = Sea((1, 2, 3))
    ship = {1, 2}
    sea.update(ship)

    print(sea.allow)
    print(sea.occupied)
