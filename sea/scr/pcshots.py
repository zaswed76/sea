#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from scr import matrix2

patterns_4 = [[[0, 1, 2, 3],
               [3, 2, 1, 0]],
              [[0, 1, 2, 3],
               [2, 3, 0, 1]]]


class Shots:
    def __init__(self):
        pass

    def random_pattern(self, deck_pattern):
        return random.choice(deck_pattern)

    def search_4_deck(self, random=False, pattern_index=0):
        if random:
            pat = self.random_pattern(patterns_4)
        else:
            pat = patterns_4[pattern_index]
        m = matrix2.Matrix(pat)
        m.create_matrix()
        return m.matrix

    def convert_matrix_to_coordinate(self, matrix):
        return list(zip(matrix[1], matrix[0]))

    def random(self, coord):
        random.shuffle(coord)
        return coord

if __name__ == '__main__':
    shots = Shots()
    mc = shots.search_4_deck()
    print(shots.convert_matrix_to_coordinate(mc))
