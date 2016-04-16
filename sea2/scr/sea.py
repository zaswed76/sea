#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libs import config
cfg = config.config('../etc/config.json')

MAX = 9
MIN = 0

class Cell(list):
    def __init__(self, y, x):
        super().__init__()
        self.extend([y, x])
        self.y = y
        self.x = x
        self.reset()

    @property
    def distance_to_obstacles_x(self):
        return self._distance_to_obstacles_x

    @distance_to_obstacles_x.setter
    def distance_to_obstacles_x(self, obstacles):
        self._distance_to_obstacles_x = obstacles - self.x

    @property
    def distance_to_obstacles_y(self):
        return self._distance_to_obstacles_y

    @distance_to_obstacles_y.setter
    def distance_to_obstacles_y(self, obstacles):
        self._distance_to_obstacles_y = obstacles - self.y

    def reset(self):
        self.horizontal_lock = False
        self.vertical_lock = False
        self.shooting = False  # стреляли ли в эту клетку
        self.ship_place = False  # размещает ли корабль весь
        self._distance_to_obstacles_x = MAX - (self.x - 1)
        self._distance_to_obstacles_y = MAX - (self.y - 1)

    def __repr__(self):
        return 'Cell - ({}, {})'.format(self.y, self.x)

if __name__ == '__main__':
    c = Cell(9, 9)
    print(c.distance_to_obstacles_x)
    print(c.distance_to_obstacles_y)