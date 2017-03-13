from collections import Set, UserDict
from new.test.cell import Cell

class Ship(UserDict):
    Horizontal = "horizontal"
    Vertical = "vertical"
    def __init__(self, sea, bow, size, vector):
        super().__init__()
        self.sea = sea
        self.bow = bow
        self.size = size
        self.vector = vector
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
        self._update_sea_status()


    def _top_cells(self):
        _y = self.bow[0] - 1
        return [(y, x) for y, x in self.around.keys() if y == _y]


    def _right_cells(self):
        _x = self.bow[1] - 1
        return [(y, x) for y, x in self.around.keys() if x == _x]


    def _update_sea_status(self):
        for _y, x in self._top_cells():
            for n in range(1, 4):
                key = (_y - n, x)
                if key in self.sea:
                    self.sea[key].vertical_allow = self.sea[(_y, x)]
        for y, _x in self._right_cells():
            for n in range(1, 4):
                key = (y, _x - n)
                if key in self.sea:
                    self.sea[key].vertical_allow = self.sea[(y, _x)]


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

    def __str__(self):
        return "bow - {}\nvector - {}\nsize - {}\nship - {}".format(self.bow,
                                                                    self.vector,
                                                                    self.size,
                                                                    self.ship.keys())