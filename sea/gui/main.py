#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from scr import sea
from gui import base

size_field = 10
ship_names = (4, 3, 3 ,2, 2, 2, 1, 1, 1, 1)

sea_cfg = sea.Config()
sea_cfg.set_size(size_field)

user_sea = sea.Sea(ship_names)
user_sea.create_field()
user_sea.create_fleet()


app = QtWidgets.QApplication(sys.argv)
main = base.Widget()
main.set_greed_pc(size_field)
main.set_greed_user(size_field)
main.show()
app.exec()




