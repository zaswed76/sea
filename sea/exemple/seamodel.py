#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy


class Cell:
    StatusEmpty = 'empty'
    StatusShip = 'ship'
    StatusHurt = 'hurt'
    StatusShot = 'shot'
    StatusNames = ['empty', 'ship', 'hurt', 'shot']

    def __init__(self, y, x):
        super().__init__()
        self.x = x
        self.y = y
        self.coord = [self.y, self.x]
        self._status = Cell.StatusEmpty

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, stat):
        if stat in Cell.StatusNames:
            self._status = stat
        else:
            raise Exception('not_name tag')

    def __repr__(self):
        return str(Cell.StatusNames.index(self.status))


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

    sea[0][0].tag = Cell.StatusShip
    print(sea)
