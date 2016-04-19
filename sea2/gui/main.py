#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys

from PyQt5 import QtWidgets

from exemple import sea, core
from gui import mainwidget
from libs import config

cfg_path = '../etc/config.json'
texture_path = '../resource/textures'

cfg = config.read_cfg(cfg_path)


class Style:
    Ship = 'ship.png'

    def __init__(self, default_style):
        self.default_style = default_style

    @property
    def texture_dir(self):
        return os.path.join(texture_path, self.default_style)

    @property
    def ship(self):
        pth = os.path.join(self.texture_dir, self.Ship)
        print(pth)
        return pth


class Main(mainwidget.MainWidget):
    def __init__(self):
        super().__init__()

        self.style = Style(cfg['default_style'])

        self.load_style_sheet(self.style.default_style)
        self.tool = mainwidget.Tool(self, cfg['tool_height'],
                                    self.tool_actions(
                                        cfg['actions_names']))
        self.init_tool_bar(self.tool)

        self.status = mainwidget.Status(self, cfg['status_height'])
        self.init_status(self.status)

        self.sea = {}

        # --- USER SEA ------
        self.sea['user'] = sea.SeaModel(0, 0, cfg['field_size'],
                                        cfg['field_size'], self,
                                        name='user', style=self.style)
        self.add_gui_sea(
            sea.View(self.sea['user'], self, size=cfg['view_size']))

        # --- PC SEA ------

        self.sea['pc'] = sea.SeaModel(0, 0, cfg['field_size'],
                                      cfg['field_size'],
                                      self,
                                      name='pc', style=self.style)
        self.add_gui_sea(
            sea.View(self.sea['pc'], self, size=cfg['view_size']))

        self.game = core.Game()

    def action_method(self, name_action):
        getattr(self, name_action)()

    # ----  ------

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

    def click_on_sea(self, scene, cell):
        m = 'click_on_sea_'
        method = '{}{}'.format(m, scene.name)
        getattr(self, method)(cell)

    def click_on_sea_pc(self, cell):
        if self.game.game_started:
            self.sea['pc'].fire(cell)
        else:
            self.sea['pc'].do_nothing()

    def click_on_sea_user(self, cell):
        if self.game.game_started:
            self.sea['user'].do_nothing()
        else:
            self.sea['user'].build_ship(cell)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()

    main.show()
    sys.exit(app.exec_())
