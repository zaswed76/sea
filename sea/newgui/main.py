#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets

from newgui import sea


class Main(sea.Sea):
    def __init__(self):
        super().__init__()
        self.create_ship('pc', (5, 8), 3, 'horizontal')
        self.create_ship('user', (2, 2), 3, 'vertical')
        self.create_ship('pc', (3, 3), 3, 'vertical')
        self.create_ship('user', (5, 5), 3, 'horizontal')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())