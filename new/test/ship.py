from collections import Set, UserDict
from new.test.cell import Cell

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
