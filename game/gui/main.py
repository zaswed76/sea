import os
import sys
from functools import partial

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QFile

from game.gui import field, tool
from game.sea import sea

actions_names = [
    "new_game.png",
    "auto_fleet_user.png",
    "settings.png",
    "SPACER",
    "style_grey.png",
    "style_writer.png",
    "close_scr.png"
]

icon_dir = r"D:\0SYNC\python_projects\workshop\sea\game\resource\icons"

class Main(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(500, 500)
        self.central = QtWidgets.QFrame(self)
        self.setCentralWidget(self.central)
        self.box = QtWidgets.QHBoxLayout(self.central)
        self.box.setSpacing(50)

        self.user_sea = sea.Sea()
        self.user_field = field.Field(self, "user", self.user_sea)
        self.box.insertWidget(0, self.user_field)
        self.user_field.update_sea()

        self.pc_sea = sea.Sea()
        self.pc_field = field.Field(self, "pc", self.pc_sea)
        self.box.insertWidget(1, self.pc_field)
        self.pc_field.update_sea()



        tool_actions = self.tool_actions(icon_dir, actions_names)
        self.tool = tool.Tool(self, tool_actions)
        self.init_tool_bar(self.tool)

    def tool_actions(self, icon_dir, names):
        actions = []
        for name in names:
            if name == tool.Tool.SPACER:
                spacer = tool.Spacer(0, 0)
                actions.append(spacer)
            else:
                name_not_ext = os.path.splitext(name)[0]
                pth = os.path.join(icon_dir, name)
                if not os.path.isfile(pth):
                    print('иконка с именем - {} не найдена'.format(pth))
                    act = tool.BtnAction(name_not_ext)
                    act.clicked.connect(
                        partial(self.action_method, name_not_ext))
                else:
                    icon = QtGui.QIcon(pth)
                    act = tool.Action(icon, name_not_ext, self)
                    act.triggered.connect(
                        partial(self.action_method, name_not_ext))
                actions.append(act)
        return actions

    def action_method(self, name_action):
        print(name_action, "!!!")
        name = name_action.split('_')[0]
        if name == 'style':
            arg = name_action.split('_')[1]
            getattr(self, 'set_' + name)(arg)
        else:

            try:
                getattr(self, name_action)()
            except AttributeError as err:
                print(err)

    def new_game(self):
        self.pc_sea.create_fleet()
        self.pc_field.clear()
        self.pc_field.update_sea()

    def auto_fleet_user(self):

        """
        очистить поле игрока
        """
        self.user_field.clear()
        # self.user_field.update_sea()

    def close_scr(self):
        self.close()

    def init_tool_bar(self, tool_bar):
        self.addToolBar(tool_bar)

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

    def wheelEvent(self, event):
        if event.angleDelta().y() / 120 > 0:
            self.pc_sea.create_fleet()
            self.field.clear()
            self.field.update_sea()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    main.load_style_sheet("grey")
    sys.exit(app.exec_())
