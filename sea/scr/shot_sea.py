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

    def append_to_left(self, y, x, n):
        lst = []
        lst.append((y, x))
        while True:
            x += n
            if x > self.max:
                return lst
            else:
                lst.append((y, x))

    def seq(self, pat, n):
        lst = []
        while True:
            for y, x in pat:
                lst.extend(self.append_to_left(y, x, n))
            pat = ()





s = Sea()
s.create_field()
print(s.append_to_left(2, 1, 4))

