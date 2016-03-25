#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scr.sea
import random



class Field:
    def __init__(self, size_field, ship_names):
        self.ship_names = ship_names
        self.sea = scr.sea.Sea()
        self.fleet = scr.sea.Fleet()
        self.sea.set_fleet(self.fleet)
        self.sea.create_field(size_field, size_field)










if __name__ == '__main__':
    names = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    pc = Field(names)
    pc.new_fleet()