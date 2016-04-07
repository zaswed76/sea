#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets

from gui5 import config
from scr import sea, pcshots
from gui5 import mainwidget, view

cfg = config.Config()


class Main(mainwidget.MainWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.load_style_sheet(cfg.default_style)
        self.tool = mainwidget.Tool(self, cfg.tool_height, self.tool_actions(cfg.actions_names))
        self.init_tool_bar(self.tool)


        self.model_user = view.SeaModel(sea.Sea(cfg.ship_names), 'user')
        self.add_gui_sea(view.View(self.model_user, self))

        self.model_pc = view.SeaModel(sea.Sea(cfg.ship_names), 'pc')
        self.add_gui_sea(view.View(self.model_pc, self))

    def action_method(self, name_action):
        try:
            getattr(self, name_action)()
        except Exception as er:
            print(er)

    def close_scr(self):
        self.close()

    def settings(self):
        print('settings')

    def new_game(self):
        print('new_game')

    def style_grey(self):
        cfg.set_config('default_style', 'style_grey')
        self.load_style_sheet('style_grey')

    def style_writer(self):
        cfg.set_config('default_style', 'style_writer')
        self.load_style_sheet('style_writer')

    def closeEvent(self, *args, **kwargs):
        config.write_cfg(config.cfg_path, cfg.config)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())