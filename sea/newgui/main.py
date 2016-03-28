#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets

from newgui import sea


class Main(sea.Sea):
    def __init__(self):
        super().__init__()
        # self.create_ship('pc', (5, 8), 2, 'horizontal')
        # self.create_ship('user', (2, 2), 1, 'vertical')
        self.create_ship('pc', (3, 3), 1, 'vertical')
        self.create_item('pc', (3, 3), 'Wounded')
        # self.create_ship('user', (5, 5), 2, 'horizontal')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())