#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile


class View(QtWidgets.QGraphicsView):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFixedSize(300, 300)


class Scene(QtWidgets.QGraphicsScene):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setSceneRect(0, 0, 300, 300)
    def mousePressEvent(self, e):
        pass
        x = e.x()
        y = e.y()
        # print(x, y)


class Sea(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        # self.setFixedSize(802, 503)
        self.loadStyleSheet('kid')

        self.main = View(self)
        self.main.move(89, 114)
        self.scene = Scene()
        self.main.setScene(self.scene)

    def loadStyleSheet(self, sheetName):
        file_name = sheetName + '.css'
        file = QFile('../css/{}'.format(file_name))
        file.open(QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        QtWidgets.QApplication.instance().setStyleSheet(styleSheet)

        # def mousePressEvent(self, e):
        #     x = e.x()
        #     y = e.y()
        #     print(x, y)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Sea()

    main.show()
    sys.exit(app.exec_())
