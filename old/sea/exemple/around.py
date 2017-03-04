#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

def showdialog(parent):
    reply = QMessageBox.question(parent, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
    if reply == QtWidgets.QMessageBox.Yes:
       return True
    else:
       return False

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.clicked.connect(self.pres_on)



    def pres_on(self):
        if showdialog(self):
            print('!!')
        else:
            print('not')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())




