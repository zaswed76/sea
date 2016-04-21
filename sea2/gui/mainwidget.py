#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
from functools import partial

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QFile

icon_dir = '../resource/icons'
texture_path = '../resource/textures'



MESSAGES = {}
MESSAGES['close'] = '''Результаты игры Не будут сохранены!
Вы действительно хотите выйти?'''

def show_dialog(parent, name_mes, message):
    box = QtWidgets.QMessageBox(parent)
    box.setIcon(QtWidgets.QMessageBox.Question)
    box.setWindowTitle(name_mes)
    box.setText(message)
    box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    buttonY = box.button(QtWidgets.QMessageBox.Yes)
    buttonY.setText('Да')
    buttonN = box.button(QtWidgets.QMessageBox.No)
    buttonN.setText('Нет')
    box.exec_()

    if box.clickedButton() == buttonY:
        return True
    # YES pressed
    elif box.clickedButton() == buttonN:
        return False


class Status(QtWidgets.QStatusBar):
    def __init__(self, parent, height):
        super().__init__(parent)
        self.setFixedHeight(height)


class Action(QtWidgets.QAction):
    def __init__(self, icon, name, parent):
        super().__init__(icon, name, parent)


class Spacer(QtWidgets.QWidget):
    def __init__(self, w, h):
        super().__init__()
        box = QtWidgets.QHBoxLayout(self)
        box.addSpacerItem(QtWidgets.QSpacerItem(w, h,
                                                QtWidgets.QSizePolicy.Expanding))


class Tool(QtWidgets.QToolBar):
    SPACER = 'SPACER'

    def __init__(self, parent, height, actions):
        super().__init__(parent)
        print(height)
        # self.setFixedHeight(height)
        self.setIconSize(QtCore.QSize(38, 38))
        self.init_actions(actions)

    def init_actions(self, actions):
        for item in actions:
            if isinstance(item, Action):
                self.addAction(item)
            elif isinstance(item, Spacer):
                self.addWidget(item)


class Style:
    Ship = 'ship.png'

    def __init__(self, default_style):
        self.default_style = default_style

    @property
    def texture_dir(self):
        return os.path.join(texture_path, self.default_style)

    @property
    def icon_dir(self):
        return os.path.join(icon_dir, self.default_style)

    @property
    def ship(self):
        pth = os.path.join(self.texture_dir, self.Ship)
        return pth

    def __str__(self):
        return " = ".join(('class', Style.__name__, self.default_style))


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._user_style = None
        self.center = QtWidgets.QFrame()
        self.center.setObjectName('center_frame')
        self.setCentralWidget(self.center)
        self.center_box = QtWidgets.QHBoxLayout(self.center)
        self.center_box.setSpacing(40)
        self.center_box.setContentsMargins(40, 30, 40, 30)


    @property
    def user_style(self):
        return self._style

    @user_style.setter
    def user_style(self, style_name):
        self._style = style_name

    def add_gui_sea(self, model_sea):
        self.center_box.addWidget(model_sea)

    def init_tool_bar(self, tool_bar):
        self.addToolBar(tool_bar)

    def init_status(self, status):
        self.setStatusBar(status)

    def tool_actions(self, icon_dir, names):
        actions = []
        for name in names:
            if name == Tool.SPACER:
                spacer = Spacer(0, 0)
                actions.append(spacer)
            else:
                name_not_ext = os.path.splitext(name)[0]
                pth = os.path.join(icon_dir, name)
                if not os.path.isfile(pth):
                    print('иконка с именем - {} не найдена'.format(pth))
                icon = QtGui.QIcon(pth)
                act = Action(icon, name_not_ext, self)
                act.triggered.connect(
                        partial(self.action_method, name_not_ext))
                actions.append(act)
        return actions

    def load_style_sheet(self, sheetName):
        """

        :param sheetName: str имя стиля
        """
        file_name = sheetName + '.css'
        file = QFile('../css/{}'.format(file_name))
        file.open(QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        QtWidgets.QApplication.instance().setStyleSheet(styleSheet)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tool = Tool()

    main = MainWidget()
    main.init_tool_bar(tool)
    main.show()
    sys.exit(app.exec_())
