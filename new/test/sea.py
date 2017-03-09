
from collections import Set, Sequence, MutableSet


class Sea(Set):

    def __init__(self):
        self._seq = set((y, x) for y in range(10) for x in range(10))
        self._allow = self._seq.copy()
        self._occupied = set()

    @property
    def allow(self):
        return self._allow

    @property
    def occupied(self):
        return self._occupied

    # def __getitem__(self, item):
    #     return list(self._seq)[item]

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
        self._occupied.update(ship)
        self._allow.difference_update(ship)



if __name__ == '__main__':

    from new.test.ship import Ship
    sea = Sea((range(100)))
    print(sea)
    ship = Ship((1, 1), 2, Ship.Horizontal)
    print(ship)
    # sea.update(ship)

