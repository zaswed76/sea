import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from game.sea.ship import Cell as MCell


class Cell(QtWidgets.QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name
        policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                       QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(policy)
        # self.setCheckable(True)
        self._actions_names = ['4v', '4>', '3v', '3>', '2v', '2>', '1']
        self.actions = [QtWidgets.QAction(n) for n in
                        ('4v', '4>', '3v', '3>', '2v', '2>', '1')]

    def action_method(self, a):
        print(a.text())

    def contextMenuEvent(self, event):
        menu = QtWidgets.QMenu(self)
        menu.addActions(self.actions)
        menu.triggered[QtWidgets.QAction].connect(self.action_method)
        menu.exec_(self.mapToGlobal(event.pos()))

    def enterEvent(self, event):
        self.setStyleSheet("border: 3px solid #59c863;")

    def leaveEvent(self, event):
        self.setStyleSheet("""border-top: 1px solid gray;
                              border-right: 1px solid gray;
                              border-bottom: none;
                              border-left: none;""")



class Field(QtWidgets.QFrame):
    def __init__(self, parent, name, sea):
        super().__init__()
        self.parent = parent
        self.sea = sea
        self.setFixedSize(500, 500)
        self.field = {}
        self.setObjectName(name)
        self._init_grid()

    def _init_grid(self):
        self.grid = QtWidgets.QGridLayout(self)
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(0, 0, 0, 0)
        for y in range(10):
            for x in range(10):
                self.field[(y, x)] = Cell((y, x))
                self.field[(y, x)].clicked.connect(self.click_cell)
                # self.field[(y, x)].setText("{},{}".format(y, x))
                self.grid.addWidget(self.field[(y, x)], y, x)

    def click_cell(self):
        obj = self.sender()
        print(obj.name)

    def clear(self):
        for k, cell in self.sea.items():
            self.field[k].setStyleSheet("background-color: #e3e3e3")

    def update_sea(self):
        for k, cell in self.sea.items():
            if cell.status == MCell.Ship:
                self.field[k].setStyleSheet("background-color: green")
                # elif cell.status == MCell.Around:
                #     self.field[k].setStyleSheet("background-color: grey")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('settings/style.qss', "r").read())
    main = Field()
    main.show()
    sys.exit(app.exec_())
