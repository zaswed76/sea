#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets

class Sea(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QGridLayout(self)


    def create_grid(self, w, h):
        for x in range(w):
            for y in range(h):
                self.box.addWidget(QtWidgets.QPushButton(str((x, y))), x, y)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Sea()
    main.create_grid(10, 10)
    main.show()
    sys.exit(app.exec_())