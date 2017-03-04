#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np


class Matr:
    def __init__(self, pattern):
        self._pattern = np.array(pattern)
        self._matrix = None

    @property
    def pattern(self):
        return self._pattern

    @property
    def matrix(self):
        return self._matrix

    def shift_right(self, matr, step):
        return np.vstack((matr[0], matr[1] + step))

    def shift_bottom(self, matr, step):
        return np.vstack((matr[0] + step, matr[1]))

    def top_line(self, matrix):
        s1 = self.shift_right(matrix, 4)
        s2 = self.shift_right(np.hsplit(matrix, 2)[1], 8)
        return np.hstack((matrix, s1, s2))

    def center(self, matrix):
        s1 = self.shift_bottom(matrix, 4)
        a = np.vstack((matrix[0][0:2], matrix[1][0:2]))
        b = np.vstack((matrix[0][4:6], matrix[1][4:6]))
        s2 = self.shift_bottom(np.hstack((a, b)), 8)
        return np.hstack((s1, s2))

    def create_matrix(self):
        top = self.top_line(self.pattern)
        center = self.center(top)
        self._matrix = np.hstack((top, center))


if __name__ == '__main__':
    pass

    lst1 = [[0, 1, 2, 3],
            [3, 2, 1, 0]]

    lst2 = [[0, 1, 2, 3],
            [2, 3, 0, 1]]

    mtr = Matr(lst1)
    mtr.create_matrix()
    print(mtr.matrix)
    print('------------------------')

    mtr2 = Matr(lst2)
    mtr2.create_matrix()
    print(mtr2.matrix)
