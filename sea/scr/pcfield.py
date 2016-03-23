#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scr.sea import Cell, Sea, Ship, Fleet
import random

class Pc:
    def __init__(self, ship_names):
        self.ship_names = ship_names

        self.sea = Sea()
        self.fleet = Fleet()
        self.sea.set_fleet(self.fleet)
        self.sea.create_field(10, 10)

    def add_fleet(self):
        for name, deck in enumerate(self.ship_names):
            # направление
            course = random.choice([Ship.Vertical, Ship.Horizontal])

            perm = self.sea.permissible(course, deck)
            bow = random.choice(perm)
            ship = Ship(bow, course, deck)
            print('имя={}; палуб={}; курс={}'.format(name, deck, course))
            print(ship.corpus)
            print(ship.top_beacon)
            print('---------------------')
            self.sea.add_ship(name, ship)
            self.sea.update_cells(ship)








if __name__ == '__main__':
    names = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    pc = Pc(names)
    pc.add_fleet()