#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets

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


    def create_grid(self, w, h):
        for x in range(w):
            for y in range(h):
                self.box.addWidget(Cell(), y, x)

    def add_ship(self):
        but = QtWidgets.QPushButton(self)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Sea()
    main.create_grid(10, 10)
    main.show()
    sys.exit(app.exec_())