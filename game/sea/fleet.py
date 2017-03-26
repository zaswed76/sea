from collections import Sequence


class Fleet(Sequence):
    def __init__(self):
        self._f = []

    def add_ship(self, ship):
        self._f.append(ship)

    def check(self):
        if self._f:
            return True
        else:
            return False

    def wound(self, item):
        pass

    def __getitem__(self, item):
        return self._f[item]

    def __contains__(self, item):
        for ship in self._f:
            if item in ship:
                return True
        else:
            return False

    def __iter__(self):
        return iter(self._f)

    def __len__(self):
        return len(self._f)

    def __str__(self):
        return "{}".format(self._f)


if __name__ == '__main__':
    fleet = Fleet()
    fleet.add_ship({1, 2, 3})
    print(3 in fleet)
    print(fleet[0])
