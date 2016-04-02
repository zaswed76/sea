#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from gui4 import config

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QFile

cfg = config.Config()

class FieldConvert:
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

class Item(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        # self.setRotation(90.0)


class SeaModel(QtWidgets.QGraphicsScene):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.model.create_field()
        size = cfg.cell_size * cfg.count_cell
        self.setSceneRect(0, 0, size, size)

        self.ships = {}
        self.field_conv = FieldConvert(320, 32, 0, 0)

    def add_fleet(self):
        self.model.create_fleet()
        for ship in self.model.fleet.values():
            self.add_ship(ship.bow, ship.course, ship.deck)


    def add_ship(self, bow, course, deck):
        x, y = self.field_conv.cell_to_coord(bow)
        print(x, y)
        # p = '../resource/textures/new/2_h.png'
        # pxm = QtGui.QPixmap(p)
        # self.ships[cell] = Item(pxm)
        # self.ships[cell].setPos(x, y)

        # self.addItem(self.ships[cell])



class View(QtWidgets.QGraphicsView):
    def __init__(self, *__args):
        super().__init__(*__args)
        size = cfg.cell_size * cfg.count_cell + 2
        self.setFixedSize(size, size)
        self.scene, self.parent = __args

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.pos().x()
        y = QMouseEvent.pos().y()
        # print(x, y)
        print(self.scene.add_ship(x, y))









class Sea(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        # self.setFixedSize(802, 503)
        self.loadStyleSheet('kid')

        self.scene = SeaModel()
        self.main = View(self.scene, self)
        self.main.move(89, 114)



    def loadStyleSheet(self, sheetName):
        file_name = sheetName + '.css'
        file = QFile('../css/{}'.format(file_name))
        file.open(QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        QtWidgets.QApplication.instance().setStyleSheet(styleSheet)


    def add_ship(self):
        p = '../resource/textures/new/4_h.png'
        pxm = QtGui.QPixmap(p)
        ship = Item(pxm)
        ship.setPos(33, 33)
        self.scene.addItem(ship)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Sea()
    main.add_ship()

    main.show()
    sys.exit(app.exec_())
