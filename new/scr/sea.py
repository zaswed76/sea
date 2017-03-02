
from new.scr import cell

class Sea:
    def __init__(self):
        self._field = {(x, y):cell.Cell(x, y) for x in range(10) for y in range(10)}

    @property
    def field(self):
        return self._field

    def __call__(self, x, y):
        return self.field[x, y]


if __name__ == '__main__':
    sea = Sea()
    sea(9, 7).status = cell.CellStatus.ship
    print(sea(9, 7).status == cell.CellStatus.ship)