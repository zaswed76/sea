#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets


from gui import mainwidget
from core import sea

action_names = ['add_ship']


class Widget(mainwidget.MainWidget):
    def __init__(self):
        super().__init__()
        self.user_style = mainwidget.Style('grey')
        self.load_style_sheet(self.user_style.default_style)

        tool_actions = self.tool_actions(self.user_style.icon_dir, action_names)
        self.tool = mainwidget.Tool(self, tool_actions)
        self.init_tool_bar(self.tool)

        self.sea = {}
        self.sea['user'] = sea.SeaModel(0, 0, 320,
                                        320, self,
                                        name='user', style=self.user_style)
        self.add_gui_sea(
                sea.View(self.sea['user'], self, size=322))


    def add_ship(self):
        print('add_ship')

    def click_right_on_sea_user(self, cell):
        print('right', cell)

    def click_left_on_sea_user(self, cell):
        print('left', cell)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.show()
    sys.exit(app.exec_())


