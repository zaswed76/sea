#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets

from newgui import field
from scr.sea import Sea
size_field = 10
ship_names = (4, 3, 3 ,2, 2, 2, 1, 1, 1, 1)


class Main(field.Sea):
    def __init__(self):
        super().__init__()
        self.init_user_sea()
        self.add_fleet_to_sea()

        # self.create_ship('pc', (5, 8), 2, 'horizontal')
        # self.create_ship('user', (2, 2), 1, 'vertical')
        # self.create_ship('pc', (3, 3), 1, 'vertical')
        # self.create_item('pc', (3, 3), 'Wounded')
        # self.create_ship('user', (5, 5), 2, 'horizontal')
    def init_user_sea(self):
        self.user_sea_model = Sea(ship_names)
        self.user_sea_model.create_field()

    def add_fleet_to_sea(self):
        self.clears()

        self.user_sea_model.create_fleet()



        for ship in self.user_sea_model.fleet.values():
            bow = (ship.x, ship.y)
            deck = ship.deck
            course = ship.course
            self.create_ship('user', bow, deck, course)



    def wheelEvent(self, *args, **kwargs):
        self.add_fleet_to_sea()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())