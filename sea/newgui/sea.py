#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap, QPalette, QBrush

from etc import config

cfg = config.Config()

size = cfg.size
user_field_coord = cfg.user_field_coord
pc_field_coord = cfg.pc_field_coord
size_cell = cfg.size_cell


def gamer_detect(x, y):
    us = user_field_coord
    pc = pc_field_coord
    user_d_x = (us[0], us[0] + size_cell * size)
    user_d_y = (us[1], us[1] + size_cell * size)
    pc_d_x = (pc[0], pc[0] + size_cell * size)
    pc_d_y = (pc[1], pc[1] + size_cell * size)

    if user_d_x[0] < x < user_d_x[1] and \
                            user_d_y[0] < y < user_d_y[1]:
        return 'user'

    if pc_d_x[0] < x < pc_d_x[1] and \
                            pc_d_y[0] < y < pc_d_y[1]:
        return 'pc'


class Field:
    def __init__(self, size, size_cell, lx, ly):
        self.size = size
        self.lx = lx
        self.ly = ly
        self.size_cell = size_cell

    def coord_to_cell(self, x, y):
        x = (x - self.lx) // (self.size_cell)
        y = (y - self.ly) // (self.size_cell)
        return (x, y)

    def cell_to_coord(self, cell):
        x, y = cell
        lx = self.size_cell * x + self.lx
        ly = self.size_cell * y + self.ly
        return lx, ly

class Ship(QtWidgets.QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)


class Sea(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(*cfg.window_size)
        self.loadStyleSheet('kid')

        self.user_field = Field(size, size_cell, *user_field_coord)
        self.pc_field = Field(size, size_cell, *pc_field_coord)
        self.gamers = dict(user=self.user_field, pc=self.pc_field)

    def loadStyleSheet(self, sheetName):
        file_name = sheetName + '.css'
        file = QFile('../css/{}'.format(file_name))
        file.open(QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        QtWidgets.QApplication.instance().setStyleSheet(styleSheet)


    def resizeEvent(self, e):
        pass

    def mousePressEvent(self, e):
        x = e.x()
        y = e.y()
        field = gamer_detect(x, y)
        try:
            cell = self.gamers[field].coord_to_cell(x, y)
            coord = self.gamers[field].cell_to_coord(cell)
            print(field, cell, coord, sep=' > ')
        except KeyError:
            print(x, y)

    def create_ship(self, field, ship):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Sea()

    main.show()
    sys.exit(app.exec_())
