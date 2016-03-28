#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QFile

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


class Item(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)

    def _pixmap(self, path):
        return QtGui.QPixmap(path)


class Ship(Item):
    def __init__(self, parent, deck, course):
        super().__init__(parent)
        self.course = course
        self.deck = deck

        self.init()

    def init(self):
        image_name = cfg.ship_names[
                         (self.deck, self.course)] + cfg.ext_img
        path = os.path.join('../resource/textures', cfg.default_style,
                            image_name)
        self.setPixmap(self._pixmap(path))

class Wounded(Item):
    def __init__(self, parent):
        super().__init__(parent)
        self.init()

    def init(self):
        image_name = cfg.wounded_item_name + cfg.ext_img
        path = os.path.join('../resource/textures', cfg.default_style,
                            image_name)
        self.setPixmap(self._pixmap(path))

class Shot(Item):
    def __init__(self, parent):
        super().__init__(parent)
        self.init()

    def init(self):
        image_name = cfg.shot_item_name + cfg.ext_img
        path = os.path.join('../resource/textures', cfg.default_style,
                            image_name)
        self.setPixmap(self._pixmap(path))

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

    def _coord(self, gamer, coord):
        x, y = self.gamers[gamer].cell_to_coord(coord)
        x_correct = x + cfg.correction[(gamer, 'x')]
        y_correct = y + cfg.correction[(gamer, 'y')]
        return x_correct, y_correct

    def create_ship(self, gamer, bow, deck, course):
        """

        :param gamer: str < pc or user
        :param bow: tuple < int
        :param deck: int << {4, 3, 2, 1}
        :param course: str << {'vertical', 'horizontal'}
        """
        x_correct, y_correct = self._coord(gamer, bow)
        ship = Ship(self, deck, course)
        ship.move(x_correct, y_correct)

    def create_item(self, gamer, bow, name, ):
        """

        :param gamer: str < pc or user
        :param bow: tuple < int
        :param deck: int << {4, 3, 2, 1}
        :param course: str << {'vertical', 'horizontal'}
        """
        x_correct, y_correct = self._coord(gamer, bow)
        item = getattr(sys.modules[__name__], name)(self)
        item.move(x_correct, y_correct)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Sea()

    main.show()
    sys.exit(app.exec_())
