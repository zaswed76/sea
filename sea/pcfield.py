#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sea import Cell, Sea, Ship
import random

class Pc:
    def __init__(self, ship_names):
        self.ship_names = ship_names

        self.sea = Sea()
        self.sea.create_field(10, 10)

    def add_fleet(self):
        for deck in self.ship_names:
            course = random.choice([Ship.Vertical, Ship.Horizontal])
            permissible = [y for y in self.sea]
            print(permissible)





if __name__ == '__main__':
    names = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    pc = Pc(names)
    pc.add_fleet()