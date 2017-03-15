

import sys
from PyQt5 import QtWidgets, QtGui

class Cell(QtWidgets.QToolButton):
    def __init__(self, *__args):
        super().__init__(*__args)
        policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                       QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(policy)
        self.setCheckable(True)
        # self.setFixedSize(100, 100)

class Field(QtWidgets.QFrame):
    def __init__(self, name):
        super().__init__()
        self.resize(500, 500)
        self.setObjectName(name)
        self._init_grid()


    def _init_grid(self):
        self.grid = QtWidgets.QGridLayout(self)
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(0, 0, 0, 0)
        for y in range(10):
            for x in range(10):
                btn = Cell()
                btn.setText("{},{}".format(y, x))
                self.grid.addWidget(btn, y, x)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('settings/style.qss', "r").read())
    main = Field()
    main.show()
    sys.exit(app.exec_())