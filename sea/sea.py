#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Cell:
    _max = 9
    _min = 0
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.shooting = False  # стреляли ли в эту клетку
        self._distance_to_obstacles_x = self._max - self.x
        self._distance_to_obstacles_y = self._max - self.y

    @property
    def distance_to_obstacles_x(self):
        return self._distance_to_obstacles_x

    @distance_to_obstacles_x.setter
    def distance_to_obstacles_x(self, obstacles):
        self._distance_to_obstacles_x = self._max - obstacles

    @property
    def distance_to_obstacles_y(self):
        return self._distance_to_obstacles_y

    @distance_to_obstacles_y.setter
    def distance_to_obstacles_y(self, obstacles):
        self._distance_to_obstacles_y = self._max - obstacles


class Sea(list):
 def __init__(self, width, height): 
        super().__init__()