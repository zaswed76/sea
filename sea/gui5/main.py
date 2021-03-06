#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets
from gui4 import service
from gui5 import config
from scr import sea, gameprocess, pcshots
from gui5 import mainwidget, view

cfg = config.Config()


class Main(mainwidget.MainWidget):
    def __init__(self):
        super().__init__()

        self.load_style_sheet(cfg.default_style)
        self.tool = mainwidget.Tool(self, cfg.tool_height, self.tool_actions(cfg.actions_names))
        self.init_tool_bar(self.tool)

        self.status = mainwidget.Status(self, cfg.status_height)
        self.init_status(self.status)

        self.pcshots = pcshots.ShellingTactics()

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
        self.service = service.Service(self)
        self.service.show()

    def clear_field(self):
        self.user_sea.clear()

    def search4(self):
        coord = self.pcshots.current
        coord = self.pcshots.convert(coord)
        # coord.sort()
        # print(type(coord))
        self.model_user.draw_items('shot', coord)

    def search4_2(self):
        coord = self.pcshots.m.search_4
        self.user_sea.draw_items('shot', coord)

    def new_game(self):
        self.auto_fleet_pc()
        if not self.model_pc.model.fleet:
            self.status.showMessage('вражеские корабли не готовы к бою')
        elif not self.model_user.model.fleet:
            self.status.showMessage('ваши корабли не готовы к бою')
        else:
            self.game()


    def style_grey(self):
        cfg.set_config('default_style', 'style_grey')
        self.load_style_sheet('style_grey')

    def style_writer(self):
        cfg.set_config('default_style', 'style_cyan')
        self.load_style_sheet('style_cyan')

    def closeEvent(self, *args, **kwargs):
        config.write_cfg(config.cfg_path, cfg.config)

    def auto_fleet_user(self):
        self.model_user.add_fleet(display=True)


    def auto_fleet_pc(self):
        self.model_pc.add_fleet(display=False)

    def click_on_cell(self, scene, x, y):
        # print(x, y, '11')
        res = scene.on_click_cell(x, y)
        self.game(result_shot = res)

    def game(self, result_shot=None):
        if result_shot is None:
            self.status.showMessage('ваш ход')

        self.shot_on_pc(*result_shot[1:])


    def shot_on_pc(self, result, message):
        print('# мы стреляем по врагу')# мы стреляем по врагу
        if result:
            self.status.showMessage('ваш ход')
        else:
            # выстрел пк
            self.shot_on_user()

    def shot_on_user(self):
        print('# по нам стреляют')# по нам стреляют
        cell = self.pcshots.next()

        res = self.model_user.auto_shot(cell)
        print(res)
        # self.click_on_cell(self.model_user, *cell)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()

    main.show()
    sys.exit(app.exec_())