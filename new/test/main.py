import random

from new.test import sea, ship, fleet

ship_names = [4]


class Main:
    def __init__(self):
        self.sea = sea.Sea(range(100))
        self.fleet = fleet.Fleet()

        # self.create_fleet()

    def create_fleet(self):
        for n in ship_names:
            vector = self._get_vector()
            bow = self._get_bow(vector, n)
            _ship = ship.Ship(bow, n, vector)
            self.sea.update(_ship)
            self.fleet.add_ship(_ship)

    def _get_bow(self, vector, size):
        cell = random.choice(list(self.sea.allow))
        self._check_ship(cell, vector, size)
        return cell

    def _check_ship(self, cell, vector, size):
        if vector == ship.Ship.Horizontal:
            for c in range(cell, cell + size):
                if c not in self.sea.allow:
                    if c == cell + size-1:
                    print(c)
                    return False
            else: return True


    def _get_vector(self):
        return random.choice((ship.Ship.Horizontal, ship.Ship.Vertical))


if __name__ == '__main__':
    mine = Main()
    print(mine._check_ship(55, ship.Ship.Horizontal, 4))
