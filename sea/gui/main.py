#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from functools import partial
from scr import sea
from gui import base

size_field = 10
ship_names = (4, 3, 3 ,2, 2, 2, 1, 1, 1, 1)

sea_cfg = sea.Config()
sea_cfg.set_size(size_field)

class Main(base.Widget):
    def __init__(self):
        super().__init__()
        self.init_user_sea()
        self.set_greed_pc(size_field)
        self.set_greed_user(size_field)


    def init_user_sea(self):
        self.user_sea_model = sea.Sea(ship_names)
        self.user_sea_model.create_field()

    def add_fleet_to_sea(self):
        self.user_sea_model.create_fleet()
        self.user_sea.reset()

        for ship in self.user_sea_model.fleet.ships_coord():
            self.add_ship(self.user_sea, ship)

    def init_actions(self):
        self.ui.settings_btn.clicked.connect(
            partial(self.loadStyleSheet, 'base'))

        self.ui.auto_btn.clicked.connect(
            partial(self.add_fleet_to_sea))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Main()
    main.show()
    app.exec()






