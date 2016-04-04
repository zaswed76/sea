#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np








class Matr:
    def __init__(self):
        pass


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
        return np.vsplit(matrix, 1)
        # s2 = self.shift_bottom(np.vsplit(matrix, 1)[0], 8)
        # return s2


    def all(self, matrix):
        top = self.top_line(matrix)
        center = self.center(top)
        return center

lst = [[0, 1, 2, 3],
       [3, 2, 1, 0]]

m = np.array(lst)
mtr = Matr()
top = mtr.top_line(m)
centr = mtr.center(top)

print(centr)


