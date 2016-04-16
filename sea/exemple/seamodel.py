#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy


class Cell:
    Status_name = {'empty': 0, 'ship': 1, 'wounded': 2, 'shot': 3}

    def __init__(self, y, x):
        super().__init__()
        self.x = x
        self.y = y
        self.coord = [self.y, self.x]
        self._status = self.Status_name['empty']

    @property
    def status(self):
        return self.Status_name[self._status]

    @status.setter
    def status(self, stat):
        self._status = self.Status_name[stat]

    def __repr__(self):
        return str(self.Status_name[self.status])


class Sea:
    min = 0
    max = 9

    def __init__(self):
        self.matrix = []

    def __getitem__(self, item):
        return self.matrix[item]

    def init_matrix(self):
        self.matrix.clear()
        _range = range(self.max + 1)
        for y in _range:
            self.matrix.append([Cell(y, x) for x in _range])


    def __repr__(self):
        return str(numpy.array(self.matrix))



if __name__ == '__main__':
    sea = Sea()
    sea.init_matrix()

    print(sea)
