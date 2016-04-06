#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
#
# m = [[0, 1, 2]] * 3
#
# b = np.array(m)
# print(b)
r = np.rot90(b, 1)
# print(r)

y1 = [0, 1, 2, 3]
x1 = [3, 2, 1, 0]

y2 = [0, 1, 2, 3]
x2 = [7, 6, 5, 4]

y3 = [4, 5, 6, 7]
x3 = [3, 2, 1, 0]

y4 = [4, 5, 6, 7]
x4 = [7, 6, 5, 4]

def shots(matrix):
    ym = [0, 1, 2, 3]
    xm = [3, 2, 1, 0]
    return [matrix[y][x] for y, x in zip(ym, xm)]

class Matrix:
    def __init__(self, size):
        self.size = size
        self.matrix = np.array(self.matr())

    def _line(self, y):
        return [(x, y) for x in range(self.size)]

    def matr(self):
        return [self._line(y) for y in range(self.size)]


m = Matrix(10)

k = shots(m.matrix)
print(k)