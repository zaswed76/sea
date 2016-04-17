#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from exemple import seamodel
from PyQt5 import QtWidgets, QtGui







class Item(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, *__args):
        super().__init__(*__args)



class SeaModel(QtWidgets.QGraphicsScene, seamodel.Sea):
    def __init__(self, *__args, name=None):
        super().__init__(*__args)
        if name is not None:
            self.name = name
        else: raise Exception('надо назначить имя сцене')

        self.x, self.y, self.width, self.height, self.parent = __args
        self.init_matrix()
        try:
            self.size_cell = self.width // len(self.matrix)
        except ZeroDivisionError:
            raise Exception('необходимо создать матрицу - поле')


    @staticmethod
    def coord_to_cell(size_cell, y, x):
        return (y // size_cell, x // size_cell)

    @staticmethod
    def cell_to_coord(size_cell, cell):
        return (size_cell * cell[0], size_cell * cell[1])



class View(QtWidgets.QGraphicsView):
    def __init__(self, *__args, size=None):
        super().__init__(*__args)
        self.setFixedSize(size, size)
        # self.scene = __args[0]
        self.parent = __args[1]

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.pos().x()
        y = QMouseEvent.pos().y()
        cell = self.scene().coord_to_cell(self.scene().size_cell, y, x)
        self.parent.click_on_sea(self.scene(), cell)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    view = View()
    scene = SeaModel()
    view.setScene(scene)
    item = Item(QtGui.QPixmap('../resource/textures/kid/1_v.png'))
    scene.addItem(item)
    view.show()
    sys.exit(app.exec_())