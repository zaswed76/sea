#!/usr/bin/env python
# -*- coding: utf-8 -*-

size = 10
lx = 90; ly = 140
rx = 370

size_cell = 28

coord = (1, 1)

def xc(x):
    return

def yc(y):
    return

def cell(x, y):
   x = (x - lx) // size_cell
   y = (y - ly) // size_cell
   return (x, y)