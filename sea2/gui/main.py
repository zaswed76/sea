#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from PyQt5 import QtWidgets

from exemple import sea, core
from gui import mainwidget
from libs import config

cfg_path = '../etc/config.json'

cfg = config.read_cfg(cfg_path)


class Main(mainwidget.MainWidget):
    def __init__(self):
        super().__init__()

        self.user_style = mainwidget.Style(cfg['default_style'])
        self.load_style_sheet(self.user_style.default_style)

        # TOOL ------------------------------------------------------

        tool_actions = self.tool_actions(self.user_style.icon_dir,
                                         cfg['actions_names'])
        self.tool = mainwidget.Tool(self, cfg['tool_height'],
                                    tool_actions)
        self.init_tool_bar(self.tool)

        # STATUS ----------------------------------------------------

        self.status = mainwidget.Status(self, cfg['status_height'])
        self.init_status(self.status)



        # GAME ------

        self.sea = {}
        self.sea['user'] = sea.SeaModel(0, 0, cfg['field_size'],
                                        cfg['field_size'], self,
                                        name='user', style=self.user_style)
        self.add_gui_sea(
                sea.View(self.sea['user'], self,
                         size=cfg['view_size']))

        # --- PC SEA ------

        self.sea['pc'] = sea.SeaModel(0, 0, cfg['field_size'],
                                      cfg['field_size'],
                                      self,
                                      name='pc', style=self.user_style)
        self.add_gui_sea(
                sea.View(self.sea['pc'], self, size=cfg['view_size']))

        self.game = core.Game()

    def closeEvent(self, e):
        ms = mainwidget.show_dialog(self, 'выход', mainwidget.MESSAGES['close'])
        if ms:
            config.write_cfg(cfg_path, cfg)
            e.accept()
        else:
            e.ignore()

    def action_method(self, name_action):
        name = name_action.split('_')[0]
        if name == 'style':
            arg = name_action.split('_')[1]
            getattr(self, 'set_' + name)(arg)
        else:
            getattr(self, name_action)()

    # ----  ------

    def set_style(self, style):
        self.user_style = mainwidget.Style(style)
        cfg['default_style'] = style
        self.load_style_sheet(style)
        self._set_sea_style(self.user_style)

    def close_scr(self):
        self.close()

    def settings(self):
        print('service')
        # self.service = service.Service(self)
        # self.service.show()

    def clear_field(self):
        self.user_sea.clear()

    def finish_game(self):
        """
        сбросить игру
        """
        self.game.game_started = False
        self.sea['pc'].the_clear()
        self.sea['user'].the_clear()

    def new_game(self):
        self.sea['user'].accept_fleet()
        print('new_game')

    def eraser(self):
        self.sea['user'].the_clear()

    def auto_fleet_user(self):
        print('auto_user')

    def auto_fleet_pc(self):
        print('auto_pc')

    def click_left_on_sea(self, scene, cell):

        """
        клик левой кнопкой мыши

        :param scene: ссылка на сцену
        :param cell: tuple < int координаты модели
        """
        m = 'click_left_on_sea_'
        method = '{}{}'.format(m, scene.name)
        getattr(self, method)(cell)

    def click_right_on_sea(self, scene, cell):

        """
        клик правой кнопкой мыши
        """
        m = 'click_right_on_sea_'
        method = '{}{}'.format(m, scene.name)
        getattr(self, method)(cell)

    def click_left_on_sea_user(self, cell):
        if self.game.game_started:
            self.sea['user'].do_nothing()
        else:
            self.sea['user'].build_ship(cell)

    def click_right_on_sea_user(self, cell):
        if self.game.game_started:
            self.sea['user'].do_nothing()
        else:
            self.sea['user'].delite_ship(cell)

    def click_right_on_sea_pc(self, cell):
        print('right_pc_click')

    def click_left_on_sea_pc(self, cell):
        print('left_pc_click')

    def _set_sea_style(self, style):
        """

        :param style: gui.mainwidget.Style
        """
        self.sea['pc'].user_style = style
        self.sea['user'].user_style = style
        self.sea['pc'].update_sea()
        self.sea['user'].update_sea()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()

    main.show()
    sys.exit(app.exec_())
