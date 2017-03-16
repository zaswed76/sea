
import sys
from PyQt5 import QtWidgets, QtCore

class Action(QtWidgets.QAction):
    def __init__(self, icon, name, parent):
        super().__init__(icon, name, parent)
        if icon:
            self.setIcon(icon)

class BtnAction(QtWidgets.QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)




class Spacer(QtWidgets.QWidget):
    def __init__(self, w, h):
        super().__init__()
        box = QtWidgets.QHBoxLayout(self)
        box.addSpacerItem(QtWidgets.QSpacerItem(w, h,
                                                QtWidgets.QSizePolicy.Expanding))


class Tool(QtWidgets.QToolBar):
    SPACER = 'SPACER'

    def __init__(self, parent, actions):
        super().__init__(parent)
        self.setIconSize(QtCore.QSize(38, 38))
        self.init_actions(actions)

    def init_actions(self, actions):
        for item in actions:
            if isinstance(item, Action):
                self.addAction(item)
            elif isinstance(item, Spacer):
                self.addWidget(item)
            else:
                self.addWidget(item)
