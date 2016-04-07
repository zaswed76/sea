#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QFile
from gui4 import config
from gui4 import service
from scr import sea, pcshots
from gui4 import view as gui
from gui.base_ui import Ui_Form

cfg = config.Config()

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.loadStyleSheet(cfg.default_style)
        self.init_actions()

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


    def loadStyleSheet(self, sheetName):
        file_name = sheetName + '.css'
        file = QFile('../css/{}'.format(file_name))
        file.open(QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        QtWidgets.QApplication.instance().setStyleSheet(styleSheet)

    def init_actions(self):
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.auto_btn.clicked.connect(self.auto_user_fleet)
        self.ui.new_game_btn.clicked.connect(self.create_pc_fleet)
        self.ui.settings_btn.clicked.connect(self.open_service)

    def auto_user_fleet(self):
        self.user_sea.add_fleet(display=True)

    def create_pc_fleet(self):
        self.pc_sea.add_fleet(display=False)

    def open_service(self):
        self.service = service.Service(self)
        self.service.show()

    def clear_field(self):
        self.user_sea.clear()

    def search4(self):
        shots = pcshots.Shots()
        mc = shots.search_4_deck(pattern_index=0)
        coord = shots.convert_matrix_to_coordinate(mc)
        # coord = shots.random(coord)
        self.user_sea.draw_items('shot', coord)

    def search4_2(self):
        shots = pcshots.Shots()
        mc = shots.search_4_deck(pattern_index=1)
        coord = shots.convert_matrix_to_coordinate(mc)
        coord = shots.random(coord)
        self.user_sea.draw_items('shot', coord)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Widget()
    main.show()
    sys.exit(app.exec_())


