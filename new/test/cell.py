
class Cell:
    Min = 0
    Max = 10
    Empty = "0"
    Ship = "8"
    Wound = "X"
    Around = "*"
    def __init__(self, y, x):
        assert (y < Cell.Max and x < Cell.Max) and (y >= Cell.Min and x >= Cell.Min)
        self.coord = (y, x)
        self.x = x
        self.y = y
        self.status = Cell.Empty
        self._vertical_allow = Cell.Max - self.y
        self._horizontal_allow = Cell.Max - self.x

    def __hash__(self):
        return hash((self.y, self.x))

    def __eq__(self, other):
        if other[1] == self.x and other[0] == self.y:
            return True
        else:
            return False

    def __getitem__(self, item):
        return self.coord[item]

    def __repr__(self):
        return "Cell-({},{})".format(*self.coord)

    @property
    def vertical_allow(self):
       return 4 if self._vertical_allow >= 4 else self._vertical_allow

    @vertical_allow.setter
    def vertical_allow(self, cell):
        """

        :param v: координата клетки которая посылает сигнал
        """
        self._vertical_allow = cell.y - self.y


    @property
    def horizontal_allow(self):
       return 4 if self._horizontal_allow >= 4 else self._horizontal_allow

    @horizontal_allow.setter
    def horizontal_allow(self, cell):
        self._horizontal_allow = cell.x - self.x

