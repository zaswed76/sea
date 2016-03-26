#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class Widget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setScaledContents(True)
        self.setAlignment(QtCore.Qt.AlignCenter)

    def set_image(self, path):
        self.setPixmap(QtGui.QPixmap(path))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.set_image('/home/vostro/project/SEA/sea/sea/resource/textures/back.png')
    main.show()
    sys.exit(app.exec_())