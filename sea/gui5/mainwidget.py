#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
from functools import partial

from PyQt5 import QtWidgets, QtGui, QtCore


icon_dir = '../resource/icons'

class Action(QtWidgets.QAction):
    def __init__(self, icon, name, parent):
        super().__init__(icon, name, parent)


class Tool(QtWidgets.QToolBar):
    def __init__(self, parent, height, actions):
        super().__init__(parent)
        self.setFixedHeight(height)
        self.setIconSize(QtCore.QSize(height, height))
        self.init_actions(actions)

    def init_actions(self, actions):
        self.addActions(actions)


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.center = QtWidgets.QFrame()
        self.setCentralWidget(self.center)
        self.center_box = QtWidgets.QHBoxLayout(self.center)

    def init_tool_bar(self, tool_bar):
        self.addToolBar(tool_bar)

    def tool_actions(self, names):
        actions = []
        for name in names:
            name_not_ext =  os.path.splitext(name)[0]
            icon = QtGui.QIcon(os.path.join(icon_dir, name))
            act = Action(icon, name_not_ext, self)
            act.triggered.connect(partial(self.action_method, name_not_ext))
            actions.append(act)
        return actions


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tool = Tool()

    main = MainWidget()
    main.init_tool_bar(tool)
    main.show()
    sys.exit(app.exec_())
