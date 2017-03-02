#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from core import seamodel as md

class Fleet(dict):
    def __init__(self):
        super().__init__()

    def __contains__(self, item):
        for ship in self.values():
            if item in ship:
                return True
        else:
            return False


def coord_to_cell(size_cell, y, x):
    print(size_cell, y, x, '11')
    return (y // size_cell, x // size_cell)


def cell_to_coord(size_cell, cell):

    """
    вниамние ! здесь имя клетки (3, 7) == (y, x)
    меняется в (x, y) -
    :param size_cell: размер клетки в пикселях
    :param cell: tuple < int координаты
    :return: координаты сцены данной клетки
    """
    return (size_cell * cell[1] + 0.5, size_cell * cell[0] + 0.5)


class Item(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, *__args):
        super().__init__(*__args)


class SeaModel(QtWidgets.QGraphicsScene):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.fleet = Fleet()
        self.matrix = []

    def __getitem__(self, item):
        return self.matrix[item]

class View(QtWidgets.QGraphicsView):
    def __init__(self, *__args, size=None):
        super().__init__(*__args)
        if size is not None:
            self.setFixedSize(size, size)
        # self.scene = __args[0]
        self.parent = __args[1]

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.pos().x
        y = QMouseEvent.pos().y
        print(self.scene().size_cell)
        cell = coord_to_cell(self.scene().size_cell, y, x)
        if QMouseEvent.buttons() & QtCore.Qt.LeftButton:
            # координаты сцены преобразоваются в координаты модели
            self.parent.click_left_on_sea(self.scene(), cell)
        else:
            self.parent.click_right_on_sea(self.scene(), cell)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    view = View(None, None)
    scene = SeaModel()
    view.setScene(scene)
    item = Item(QtGui.QPixmap('../resource/textures/kid/1_v.png'))
    scene.addItem(item)
    view.show()
    sys.exit(app.exec_())