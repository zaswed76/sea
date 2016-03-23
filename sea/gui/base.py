#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets
from gui.base_ui import Ui_Form

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.ui = Ui_Form()
        self.ui.setupUi(self)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()

    main.show()
    app.exec()