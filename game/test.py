


import sys
from PyQt5 import QtWidgets

class Cell:
    def __init__(self, parent=None, x=0, y=0):
        self.y = y
        self.x = x
        print(y - x)


class Widget(QtWidgets.QLabel, Cell):
    def __init__(self, parent, x, y):
        super().__init__()
        self.resize(500, 500)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget(None, 1, 1)
    main.show()
    sys.exit(app.exec_())