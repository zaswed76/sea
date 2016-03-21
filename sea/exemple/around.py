#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sea import Cell, Sea, Ship


ship = Ship((5, 5), Ship.Horizontal, 2)
sea = Sea()
sea.create_field(10, 10)
sea.add_ship(ship)



# for x, y in left:
#     for n in range(-4, 0):



# print(list(range(-4, 0)))



