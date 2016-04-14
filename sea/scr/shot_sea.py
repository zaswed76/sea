#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gui5 import config
from scr import sea

cfg = config.Config()

patterns_4 = [(0, 3), (1, 2), (2, 1), (3, 0)]




class Sea(sea.Sea):
    max = 9
    def __init__(self):
        super().__init__()
        self.search_4 = []
        self.search_3 = []
        self.search_2 = []
        self.search_1 = []

    def append_to_left(self, y, x, n):
        lst = []
        lst.append((x, y))
        while True:
            x += n
            if x > self.max:
                return lst
            else:
                lst.append((x, y))

    def top(self, pat, n):
        lst = []
        for x, y in pat:
            lst.extend(self.append_to_left(x, y, n))
        return lst

    def append_to_bottom(self, x, y, n):
        lst = []
        lst.append((x, y))
        while True:
            y += n
            if y > self.max:
                return lst
            else:
                lst.append((x, y))

    def create_shots(self, pat, n):
        top = self.top(pat, 4)
        for x, y in top:
            self.search_4.extend(self.append_to_bottom(x, y, n))





s = Sea()
s.create_field()
s.create_shots(patterns_4, 4)
print(s.search_4)



