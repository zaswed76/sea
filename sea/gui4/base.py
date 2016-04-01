#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QFile
from gui3 import view
from gui.base_ui import Ui_Form

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.loadStyleSheet('kid')


        self.user_sea = view.SeaModel()
        self.add_sea(self.user_sea, self.ui.frame_gamer_Grid)

        self.pc_sea = view.SeaModel()
        self.add_sea(self.pc_sea, self.ui.frame_pc_Grid)

    def add_sea(self, sea, field):
        _view = view.View(sea, self)
        box = QtWidgets.QVBoxLayout(field)
        box.setContentsMargins(0,0,0,0)
        box.addWidget(_view)


    def loadStyleSheet(self, sheetName):
        file_name = sheetName + '.css'
        file = QFile('../css/{}'.format(file_name))
        file.open(QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        QtWidgets.QApplication.instance().setStyleSheet(styleSheet)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Widget()
    main.show()
    sys.exit(app.exec_())


