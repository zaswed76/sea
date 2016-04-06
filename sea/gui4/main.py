#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import time

from PyQt5 import QtWidgets, QtGui
from gui4 import view as gui
from scr import sea, pcshots
from gui4 import config, service

cfg = config.Config()

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.center = QtWidgets.QFrame()
        self.setCentralWidget(self.center)
        self.hbox = QtWidgets.QHBoxLayout(self.center)

        self.user_model = sea.Sea(cfg.ship_names)
        self.user_sea = gui.SeaModel(self.user_model, 'user')
        self.add_sea(self.user_sea, self.ui.frame_gamer_Grid)

        self.pc_model = sea.Sea(cfg.ship_names)
        self.pc_sea = gui.SeaModel(self.pc_model, 'pc')
        self.add_sea(self.pc_sea, self.ui.frame_pc_Grid)

    def add_sea(self, sea, field):
        _view = gui.View(sea, self)
        box = QtWidgets.QVBoxLayout(field)
        box.setContentsMargins(0,0,0,0)
        box.addWidget(_view)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Main()
    main.show()
    sys.exit(app.exec_())

