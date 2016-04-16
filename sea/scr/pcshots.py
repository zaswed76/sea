#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from scr import shot_sea
#
# patterns_4 = [[[0, 1, 2, 3],
#                [3, 2, 1, 0]],
#               [[0, 1, 2, 3],
#                [2, 3, 0, 1]]]

patterns_4 = [(3, 0), (2, 1), (1, 2), (0, 3)]
patterns_4_2 = [(3, 0), (2, 1), (0, 2), (1, 3)]


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
        m = shot_sea.Sea()
        m.create_field()
        m.create_shots(pat, 4)
        return m.search_4

    def convert_matrix_to_coordinate(self, matrix):
        return list(zip(matrix[1], matrix[0]))

    def random(self, coord):
        random.shuffle(coord)
        return coord


class ShellingTactics:
    def __init__(self):
        self._current = []
        self.cursor = 0
        self.m = shot_sea.Sea()
        self.m.create_field()
        self.m.create_shots(patterns_4_2, 4)

    @property
    def current(self):
        return self.m.search_4


    def convert(self, coords):
         return [(y, x) for x, y in coords]

    def next(self):
        cell = self.m.search_4[self.cursor]
        self.cursor += 1
        return cell


if __name__ == '__main__':
    shots = ShellingTactics()
    print(shots.next())
