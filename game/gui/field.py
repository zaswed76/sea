

import sys
from PyQt5 import QtWidgets

class Cell(QtWidgets.QToolButton):
    def __init__(self, *__args):
        super().__init__(*__args)

class Field(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.box = QtWidgets.QHBoxLayout(self)
        self.btn = Cell(self)
        self.box.addWidget(self.btn)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('settings/style.qss', "r").read())
    main = Field()
    main.show()
    sys.exit(app.exec_())