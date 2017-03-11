import random

from new.test import sea, ship, fleet

ship_names = [4]


class Pc:
    def __init__(self):
        self.sea = sea.Sea()
        self.fleet = fleet.Fleet()

    def __repr__(self):
        return "{}".format(self.sea)

    def create_fleet(self):
        for size in ship_names:
            vector = self._get_vector()
            bow = self._get_bow(size, vector)
            _ship = ship.Ship(bow, size, vector)
            self.fleet.add_ship(_ship)
            self.sea.update(_ship)




    def _get_vector(self):
        return random.choice((ship.Ship.Horizontal, ship.Ship.Vertical))

    def _get_bow(self, size, vector):
        if vector == ship.Ship.Horizontal:
            allow = self._get_hor_allow(size)
            return random.choice(allow)
        elif vector == ship.Ship.Vertical:
            allow = self._get_ver_allow(size)
            return random.choice(allow)

    def _get_hor_allow(self, name):
        a = []
        for cell in self.sea:
            if cell.horizontal_allow == name:
                a.append(cell)
        return a

    def _get_ver_allow(self, name):
        a = []
        for cell in self.sea:
            if cell.vertical_allow == name:
                a.append(cell)
        return a



if __name__ == '__main__':
    pc = Pc()
    pc.create_fleet()
    c = pc.fleet[0].bow
    # print(pc.fleet[0].all)
    # print(pc.fleet[0].around)
    print(type(c))
    print(c.x)
    print(c.status)
    print(c in pc.fleet)
    # print(c in pc.fleet)


