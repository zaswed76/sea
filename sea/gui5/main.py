#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets

from gui5 import config
from gui5 import mainwidget

cfg = config.Config()


class Main(mainwidget.MainWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.tool = mainwidget.Tool(self, cfg.tool_height, self.tool_actions(cfg.actions_names))
        self.init_tool_bar(self.tool)

    def action_method(self, name_action):
        print(name_action)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Main()
    main.show()
    sys.exit(app.exec_())