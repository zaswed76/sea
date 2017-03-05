
from new.scr import cell

class Sea:
    def __init__(self):
        self._field = set(cell.Cell(x, y) for x in range(10) for y in range(10))
        self.occupied_space = set()


    @property
    def field(self):
        return self._field

    def create_fleet(self):
        pass

    def create_ship(self, bow, size, vector):
        pass

    def get_bow(self, size, vector):
        """
        :return координаты носа корабля
        """
        pass

    def building_allow(self, bow, size, vector):
        x, y = bow
        if vector == "horizontal":
            s = [x for x in range(size)]





    def get_vector(self):
        """
        :return направление  vertical or horizontal
        """
        pass

    def __call__(self, x, y):
        return self.field[x, y]


if __name__ == '__main__':
    sea = Sea()
    print(sea.field)