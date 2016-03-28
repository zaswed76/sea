#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets

from newgui import sea


class Main(sea.Sea):
    def __init__(self):
        super().__init__()
        # self.create_ship('pc', 1)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())