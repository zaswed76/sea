#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtWrapperType
from abc import ABCMeta

class FinalMeta(pyqtWrapperType, ABCMeta):
    pass

class Cell(list):
    def __init__(self):
        super().__init__()


class Item(Cell, QtWidgets.QGraphicsPixmapItem, metaclass=FinalMeta):
    def __init__(self, *__args):
        Cell.__init__(self)
        QtWidgets.QGraphicsPixmapItem.__init__(self)


class SeaModel(QtWidgets.QGraphicsScene):
    def __init__(self, *__args):
        super().__init__(*__args)


class View(QtWidgets.QGraphicsView):
    def __init__(self, *__args):
        super().__init__(*__args)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    view = View()
    scene = SeaModel()
    view.setScene(scene)
    item = Item(QtGui.QPixmap('../resource/textures/kid/1_v.png'))
    scene.addItem(item)
    view.show()
    sys.exit(app.exec_())