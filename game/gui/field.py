

import sys
from PyQt5 import QtWidgets, QtGui
from game.sea.ship import Cell as MCell

class Cell(QtWidgets.QToolButton):
    def __init__(self, *__args):
        super().__init__(*__args)
        policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                       QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(policy)
        self.setCheckable(True)
        # self.setFixedSize(100, 100)

class Field(QtWidgets.QFrame):
    def __init__(self, name, sea):
        super().__init__()
        self.sea = sea
        self.resize(500, 500)
        self.field = {}
        self.setObjectName(name)
        self._init_grid()

    def _init_grid(self):
        self.grid = QtWidgets.QGridLayout(self)
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(0, 0, 0, 0)
        for y in range(10):
            for x in range(10):
                self.field[(y, x)] = Cell()
                self.field[(y, x)].setText("{},{}".format(y, x))
                self.grid.addWidget(self.field[(y, x)], y, x)

    def update_sea(self):
        for k, cell in self.sea.items():
            if cell.status == MCell.Ship:
                self.field[k].setChecked(True)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('settings/style.qss', "r").read())
    main = Field()
    main.show()
    sys.exit(app.exec_())