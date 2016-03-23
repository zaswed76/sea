#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile

from gui.base_ui import Ui_Form


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_setting()
        self.resize(500, 500)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.loadStyleSheet(self.default_style)
        self.init_actions()

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
    main.show()
    app.exec()
