import random
import copy
from collections import UserDict
import numpy
from game.sea.fleet import Fleet
from game.sea.ship import Ship
from game.sea.cell import Cell

class Sea(UserDict):
    def __init__(self):
        super().__init__()
        self.ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.data.update({(y, x):Cell(y, x) for y in range(10) for x in range(10)})
        self.data_copy = copy.deepcopy(self.data)
        self.fleet = Fleet()

    def create_fleet(self):
        self.data.clear()
        self.data.update({(y, x):Cell(y, x) for y in range(10) for x in range(10)})
        for size in self.ship_sizes:
            vector = random.choice((Ship.Horizontal, Ship.Vertical))
            bow = random.choice(self._get_allow_field(vector, size))
            ship = self._create_ship(self, bow, size, vector)
            self.fleet.add_ship(ship)

    def _create_ship(self, sea,  bow, size, vector):
        return Ship(sea, bow, size, vector)

    def _get_allow_field(self, vector, size):
        d = {}
        if vector == Ship.Horizontal:
            for k, cell in self.items():
                if (cell.horizontal_allow >= size and
                        cell.status == Cell.Empty):
                    d[k] = cell
        elif vector == Ship.Vertical:
            for k, cell in self.items():
                if (cell.vertical_allow >= size and
                    cell.status == Cell.Empty):
                    d[k] = cell
        return list(d.values())

    def clear(self):
        for cell in self.data.values():
            cell.status = Cell.Empty


    def __str__(self):
        lst = [x.status for x in self.data.values()]
        r = numpy.array([lst[i:i+10] for i in range(0,len(lst),10)])
        return str(r)




if __name__ == '__main__':
    sea = Sea()
    sea.create_fleet()
    print(sea)








    # cell = Cell(7, 3)
    # cell2 = Cell(7, 5)
    # cell.horizontal_allow = cell2
    # print(cell.horizontal_allow)
