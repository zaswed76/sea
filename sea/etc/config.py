#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Config:
    def __init__(self):
        self.default_style = 'kid'
        self.ext_img = '.png'
        self.ship_names = {(4, 'vertical'): '4_v',
                           (4, 'horizontal'): '4_h',
                           (3, 'vertical'): '3_v',
                           (3, 'horizontal'): '3_h',
                           (2, 'vertical'): '2_v',
                           (2, 'horizontal'): '2_h',
                           (1, 'vertical'): '1_v'}

        self.shot_item_name = 'shot'
        self.wounded_item_name = 'wounded'

        self.size = 10
        self.user_field_coord = (90, 144)
        self.pc_field_coord = (455, 144)
        self.size_cell = 28
        self.window_size = (802, 503)

        self.correction = {('pc', 'y'): -2,
                           ('pc', 'x'): 0,
                           ('user', 'y'): 0,
                           ('user', 'x'): 0}
