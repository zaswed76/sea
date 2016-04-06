#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets, QtGui

class Service(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.box = QtWidgets.QVBoxLayout(self)
        self.clear_field()
        self.search4()
        self.search4_2()

    def clear_field(self):
        clear_btn = QtWidgets.QPushButton('clear')
        self.box.addWidget(clear_btn)
        clear_btn.clicked.connect(self.parent.clear_field)

    def search4(self):
        search4_btn = QtWidgets.QPushButton('search4')
        self.box.addWidget(search4_btn)
        search4_btn.clicked.connect(self.parent.search4)

    def search4_2(self):
        search4_btn = QtWidgets.QPushButton('search4_2')
        self.box.addWidget(search4_btn)
        search4_btn.clicked.connect(self.parent.search4_2)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Service()
    main.show()
    sys.exit(app.exec_())