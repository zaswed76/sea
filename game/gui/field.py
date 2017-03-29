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
        # self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.parent = parent
        self.name = (y, x)
        self.y, self.x = y, x
        self.status = MCell.Empty
        self.setFixedSize(50, 50)
        # policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
        #                                QtWidgets.QSizePolicy.Expanding)
        # self.setSizePolicy(policy)
        # self.setCheckable(True)

        self.actions = [QtWidgets.QAction(n) for n in
                        ACTIONS_NAMES.keys()]

    def draw_ship(self):
        self.setStyleSheet("background-color: #21BBD4")

    def draw_shot(self):
        self.setText("*")

    def draw_wound_ship(self):
        self.setText("X")

    def action_method(self, a):
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

    def clear(self):
        self.setText("")

    def mousePressEvent(self, *args, **kwargs):
        if self.parent.objectName() == "pc":
            self.parent.shot(self.name)




class Field(QtWidgets.QFrame):
    def __init__(self, parent, name, sea):
        super().__init__()
        self.parent = parent

        self.sea = sea
        self.setFixedSize(500, 500)
        self.field = {}
        self.setObjectName(name)
        self._init_grid()


    def shot(self, cell):
        self.parent.user_shot(cell)


    def click_cell(self):
        obj = self.sender()
        print(obj.name)

    def clear(self):
        for k, cell in self.sea.items():
            self.field[k].setStyleSheet("background-color: #e3e3e3")
            self.field[k].status = MCell.Empty
            self.field[k].clear()

    def update_sea(self):
        for k, cell in self.sea.items():
            if cell.status == MCell.Ship:
                self.field[k].draw_ship()
                self.field[k].status = MCell.Ship
            elif cell.status == MCell.Around:
                self.field[k].status = MCell.Around
            elif cell.status == MCell.Shot or cell.status == MCell.AroundShot:
                self.field[k].draw_shot()
            elif cell.status == MCell.WoundShip:
                self.field[k].setText("X")

    def create_ship(self, bow, ship_name):
        self.parent.create_ship(bow, ship_name)

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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('settings/style.qss', "r").read())
    main = Field()
    main.show()
    sys.exit(app.exec_())
