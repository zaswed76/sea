#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from PyQt5 import QtWidgets

from exemple import sea
from gui import mainwidget
from libs import config

cfg_path = '../etc/config.json'
cfg = config.read_cfg(cfg_path)

class Game:
    def __init__(self):
        pass

    def action_method(self, name_action):
        getattr(self, name_action)()

    # ---- метдоды обработки сигналов действий пользователя ------

    def close_scr(self):
        self.close()

    def settings(self):
        print('service')
        # self.service = service.Service(self)
        # self.service.show()

    def clear_field(self):
        self.user_sea.clear()

    def new_game(self):
        print('new_game')

    def style_grey(self):
        print('load style')
        # cfg.set_config('default_style', 'style_grey')
        # self.load_style_sheet('style_grey')

    def style_writer(self):
        print('load style')
        # cfg.set_config('default_style', 'style_writer')
        # self.load_style_sheet('style_writer')

    def closeEvent(self, *args, **kwargs):
        print('close')
        sys.exit()

    def auto_fleet_user(self):
        print('auto_user')

    def auto_fleet_pc(self):
        print('auto_pc')

    def click_on_sea(self, scene, y, x):
        m = 'click_on_sea_'
        method = '{}{}'.format(m, scene.name)
        getattr(self, method)(y, x)

    def click_on_sea_pc(self, y, x):
        print(y, x, 'pc')

    def click_on_sea_user(self, y, x):
        print(y, x, 'user')


class Main(mainwidget.MainWidget, Game):
    def __init__(self):
        super().__init__()

        self.load_style_sheet(cfg['default_style'])
        self.tool = mainwidget.Tool(self, cfg['tool_height'],
                                    self.tool_actions(
                                            cfg['actions_names']))
        self.init_tool_bar(self.tool)

        self.status = mainwidget.Status(self, cfg['status_height'])
        self.init_status(self.status)

        self.model_sea = {}

        # --- USER SEA ------
        self.model_sea['user'] = sea.SeaModel(0, 0, cfg['field_size'],
                                     cfg['field_size'], self, name='user')
        self.add_gui_sea(
            sea.View(self.model_sea['user'], self, size=cfg['view_size']))

        # --- PC SEA ------

        self.model_sea['pc'] = sea.SeaModel(0, 0, cfg['field_size'],
                                     cfg['field_size'], self, name='pc')
        self.add_gui_sea(
            sea.View(self.model_sea['pc'], self, size=cfg['view_size']))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()

    main.show()
    sys.exit(app.exec_())
