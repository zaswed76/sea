#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scr.sea
import random


class Player_turn:
    def __init__(self):
        self.message = 'ход игрока'


class Game:
    status = {'Player_turn': Player_turn, 'Pc_turn': 'Pc turn',
              'Game_over': 'Game_over'}

