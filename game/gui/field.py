import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from game.sea.ship import Cell as MCell
from game.sea.ship import Ship

ACTIONS_NAMES = {
    '4v': (4, Ship.Vertical),
    '4>': (4, Ship.Horizontal),
    '3v': (3, Ship.Vertical),
    '3>': (3, Ship.Horizontal),
    '2v': (2, Ship.Vertical),
    '2>': (2, Ship.Horizontal),
    '1': (1, Ship.Vertical)}


class Cell(QtWidgets.QPushButton, MCell):
    def __init__(self, parent=None, y=0, x=0):
        super().__init__()

        self.parent = parent
        self.name = (y, x)
        self.y, self.x = y, x
        self.status = MCell.Empty
        policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                       QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(policy)
        # self.setCheckable(True)

        self.actions = [QtWidgets.QAction(n) for n in
                        ACTIONS_NAMES.keys()]

    def action_method(self, a):
        print( "!!!", ACTIONS_NAMES[a.text()], self.name)
        self.parent.create_ship(self.name, ACTIONS_NAMES[a.text()])

    def contextMenuEvent(self, event):

        if self.status == MCell.Empty:

            menu = QtWidgets.QMenu(self)
            menu.addActions(self.actions)
            menu.triggered[QtWidgets.QAction].connect(self.action_method)

            menu.exec_(self.mapToGlobal(event.pos()))

    def enterEvent(self, event):
        if self.status == MCell.Empty:
            self.setStyleSheet("border: 3px solid #59c863;")

    def leaveEvent(self, event):
        if self.status == MCell.Empty:
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
                self.field[(y, x)] = Cell(parent=self, y=y, x=x)
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
        # print(self.sea)
        for k, cell in self.sea.items():
            if cell.status == MCell.Ship:
                self.field[k].setStyleSheet("background-color: green")
                self.field[k].status = MCell.Ship
            elif cell.status == MCell.Around:
                self.field[k].status = MCell.Around

    def create_ship(self, bow, ship_name):

        self.parent.create_ship(bow, ship_name)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('settings/style.qss', "r").read())
    main = Field()
    main.show()
    sys.exit(app.exec_())
