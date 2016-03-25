#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

from collections import UserDict
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QFile, Qt

from gui.base_ui import Ui_Form


from PyQt5.QtCore import pyqtWrapperType
from abc import ABCMeta


texture_ship = '../resource/textures/ship.png'
texture_wounded = '../resource/textures/wounded.png'

class FinalMeta(pyqtWrapperType, ABCMeta):
    pass

class Cell(QtWidgets.QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setCheckable(True)
        self.setFixedSize(80, 80)
        # self.setIconSize(QtCore.QSize(40, 40))
        # self.setAlignment(Qt.AlignCenter)
        # self.setScaledContents(True)

    def add_ship(self):
        self.setChecked(True)

    def reset(self):
        self.setChecked(False)




class Sea(QtWidgets.QFrame, UserDict, metaclass=FinalMeta):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QGridLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.sea = {}

    def reset(self):
        for cell in self.values():
            cell.reset()


    def create_grid(self, size):
        lst = range(size)
        for x in lst:
            for y in lst:
                self[(x, y)] = Cell()
                self.box.addWidget(self[(x, y)], y, x)

    def add_ship(self, bow, course, deck):
        but = QtWidgets.QPushButton(self)

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.init_setting()
        self.resize(500, 500)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.loadStyleSheet(self.default_style)
        self.init_actions()

    def set_greed_pc(self, size):
        left = self.ui.frame_pc_Grid
        box = QtWidgets.QVBoxLayout(left)
        box.setContentsMargins(0,0,0,0)
        self.pc_sea = Sea()
        self.pc_sea.create_grid(size)
        box.addWidget(self.pc_sea)

    def set_greed_user(self, size):
        left = self.ui.frame_gamer_Grid
        box = QtWidgets.QVBoxLayout(left)
        box.setContentsMargins(0,0,0,0)
        self.user_sea = Sea()
        self.user_sea.create_grid(size)
        box.addWidget(self.user_sea)

    def init_setting(self):
        self.default_style = 'kid'

    def loadStyleSheet(self, sheetName):
        file_name = sheetName + '.css'
        file = QFile('../css/{}'.format(file_name))
        file.open(QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        QtWidgets.QApplication.instance().setStyleSheet(styleSheet)



    def add_ship(self, sea, ship):
        for cell in ship:
            sea[cell].add_ship()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.set_greed_pc()
    main.set_greed_user()
    main.show()
    app.exec()
