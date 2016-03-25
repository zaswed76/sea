#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, Qt

from gui.base_ui import Ui_Form


class Cell(QtWidgets.QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFixedSize(40, 40)


class Sea(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QGridLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.sea = {}


    def create_grid(self, size):
        lst = range(size)
        for x in lst:
            for y in lst:
                self.sea[(x, y)] = Cell()
                self.box.addWidget(self.sea[(x, y)], y, x)

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

    def init_actions(self):
        self.ui.settings_btn.clicked.connect(
            partial(self.loadStyleSheet, 'base'))

        self.ui.auto_btn.clicked.connect(
            partial(self.auto_create_user_fleet))

    def auto_create_user_fleet(self):
        print('!!')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.set_greed_pc()
    main.set_greed_user()
    main.show()
    app.exec()
