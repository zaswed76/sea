#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A:
    d = {}
    d['x'] = 0
    def __getattr__(self, item):
        return self.d[item]

a = A()
print(a.x)