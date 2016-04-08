#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scr.sea
import random


class Player_turn:
    def __init__(self):
        self.message = 'ход игрока'


class GameProcess:
    status = {'Player_turn': Player_turn, 'Pc_turn': 'Pc turn',
              'Game_over': 'Game_over'}


    def user_fleet(self):
        return True

    def pc_fleet(self):
        return True

    def game(self):
        while True:
            pass

    def shot(self, result_shot):
        print(result_shot)


