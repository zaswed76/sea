#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, Qt

from gui.base_ui import Ui_Form
from gui import sea


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

    def set_greed_pc(self):
        left = self.ui.frame_pc_Grid
        box = QtWidgets.QVBoxLayout(left)
        box.setContentsMargins(0,0,0,0)
        self.pc_sea = sea.Sea()
        self.pc_sea.create_grid(10, 10)
        box.addWidget(self.pc_sea)

    def set_greed_user(self):
        left = self.ui.frame_gamer_Grid
        box = QtWidgets.QVBoxLayout(left)
        box.setContentsMargins(0,0,0,0)
        self.user_sea = sea.Sea()
        self.user_sea.add_ship()
        self.user_sea.create_grid(10, 10)
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.set_greed_pc()
    main.set_greed_user()
    main.show()
    app.exec()
