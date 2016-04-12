#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[3, 6, 9],
     [2, 5, 8],
     [1, 4, 7]]


def vertical(m, n):
    return [x[n] for x in m]


def vertical2(m, n):
    return list(map(lambda x: x[n], m))


def rot(m):
    lst = []
    for n in reversed(range(len(m))):
        lst.append(vertical2(m, n))
    return lst


def rot2(m):
    return [list(map(lambda x: x[n], m)) for n in
            range(len(m), 0, -1)]


print(rot2(a))
