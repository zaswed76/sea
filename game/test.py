


import sys
from PyQt5 import QtWidgets

class Cell:
    def __init__(self, x=0, y=0):
        pass

class Widget(QtWidgets.QFrame, Cell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(500, 500)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('settings/style.qss', "r").read())
    main = Widget(None, x=1, y=1)
    main.show()
    sys.exit(app.exec_())