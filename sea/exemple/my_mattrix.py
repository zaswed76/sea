#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint

patterns_4 = [[0, 1, 2, 3],
              [3, 2, 1, 0]]

a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
     ]


class Matrix:
     def __init__(self, matrix):
         self.matrix = matrix

     def diagonal(self, start):
          for i in range(len(self.matrix) - start):
               self.matrix[i][start + i] = 1

     def display(self):
          return pprint.pprint(self.matrix)


m = Matrix(a)
m.diagonal(6)
m.diagonal(2)
m.display()



