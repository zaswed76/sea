#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QFile

from gui4 import config

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

    def coord_to_cell_coord(self, x, y):
        cell = self.coord_to_cell(x, y)
        return self.cell_to_coord(cell)


class Item(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        # self.setRotation(90.0)


class SeaModel(QtWidgets.QGraphicsScene):
    def __init__(self, model, name_model):
        super().__init__()
        self.name_model = name_model
        self.model = model
        self.model.create_field()
        size = cfg.cell_size * cfg.count_cell
        self.setSceneRect(0, 0, size, size)
        self._items = {}
        self.field_conv = FieldConvert(320, 32, 0, 0)

    def add_fleet(self, display=False):
        self.clear()
        self.model.create_fleet()
        if display:
            for ship in self.model.fleet.values():
                self.add_ship(ship)

    def on_click_cell(self, x, y):
        if self.name_model == 'user':
            self.user_click(x, y)
        else:
            self.pc_click(x, y)

    def user_click(self, x, y):
        print('user', x, y)

    def pc_click(self, x, y):

        cell = self.field_conv.coord_to_cell(x, y)
        shot_res, status, name = self.model.fleet.shot(cell)
        x, y = self.field_conv.coord_to_cell_coord(x, y)
        if shot_res:
            self.add_item(x, y, 'wounded')
        else:
            self.add_item(x, y, 'shot')
        if status == 'kill':
            self.draw_ship(name)
            self.draw_items_around(name, 'shot')

    def draw_items_around(self, ship_name, item_name):
        for cell in self.model.fleet[ship_name].around:
            x, y = self.field_conv.cell_to_coord(cell)
            self.add_item(x, y, item_name)

    def draw_items(self, item_name, coordinates):
        for cell in coordinates:
            x, y = self.field_conv.cell_to_coord(cell)
            self.add_item(x, y, item_name)
            QtWidgets.qApp.processEvents()
            time.sleep(0.2)


    def draw_ship(self, name):
        self.add_ship(self.model.fleet[name])

    def add_item(self, x, y, item_name):
        name = '{}.{}'.format(item_name, cfg.ext)
        path = os.path.join('../resource/textures',
                            cfg.default_style, name)
        self.draw_item((x, y), path, x, y)

    def draw_item(self, name, path, x, y):
        pxm = QtGui.QPixmap(path)
        self._items[name] = Item(pxm)
        print(x, y)
        self._items[name].setPos(x, y)
        self.addItem(self._items[name])

    def add_ship(self, ship):
        x, y = self.field_conv.cell_to_coord(ship.bow)
        name = '{}_{}.{}'.format(ship.deck, ship.course, cfg.ext)
        path = os.path.join('../resource/textures',
                            cfg.default_style, name)

        pxm = QtGui.QPixmap(path)
        self._items[ship.name] = Item(pxm)
        self._items[ship.name].setPos(x, y)
        self._items[ship.name].setFlag(
            QtWidgets.QGraphicsItem.ItemStacksBehindParent, True)

        self.addItem(self._items[ship.name])


class View(QtWidgets.QGraphicsView):
    def __init__(self, *__args):
        super().__init__(*__args)
        size = cfg.cell_size * cfg.count_cell + 2
        self.setFixedSize(size, size)
        self.scene, self.parent = __args

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.pos().x()
        y = QMouseEvent.pos().y()
        self.scene.on_click_cell(x, y)


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
