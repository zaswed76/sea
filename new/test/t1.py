

import sys
from PyQt5 import QtWidgets


class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.btn = QtWidgets.QPushButton(self)
        self.btn.clicked.connect(self.show_wind)

    def show_wind(self):
        self.wind = QtWidgets.QFrame()
        self.wind.resize(200, 200)
        self.wind.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.show()
    sys.exit(app.exec_())
