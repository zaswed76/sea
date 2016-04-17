#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from exemple import seamodel
from PyQt5 import QtWidgets, QtGui





class Item(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, *__args):
        super().__init__(*__args)



class SeaModel(QtWidgets.QGraphicsScene, seamodel.Sea):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'SEA'




class View(QtWidgets.QGraphicsView):
    def __init__(self, *__args, size=None):
        super().__init__(*__args)
        self.setFixedSize(size, size)
        self.parent = __args[1]

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.pos().x()
        y = QMouseEvent.pos().y()
        print(x, y, self.scene().name)
        # self.parent.click_on_cell(self.scene, x, y)

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