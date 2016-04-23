#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from core import seamodel as md



def coord_to_cell(size_cell, y, x):
    print(size_cell, y, x, '11')
    return (y // size_cell, x // size_cell)


def cell_to_coord(size_cell, cell):

    """
    вниамние ! здесь имя клетки (3, 7) == (y, x)
    меняется в (x, y) -
    :param size_cell: размер клетки в пикселях
    :param cell: tuple < int координаты
    :return: координаты сцены данной клетки
    """
    return (size_cell * cell[1] + 0.5, size_cell * cell[0] + 0.5)


class Item(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, *__args):
        super().__init__(*__args)


class SeaModel(QtWidgets.QGraphicsScene):
    def __init__(self, *__args, name=None, style=None):
        super().__init__(*__args)
        self.ships = {}
        self._user_style = style
        self._fleet = md.Fleet()
        self.model = md.Sea(self._fleet)
        if name is not None:
            self.name = name
        else:
            raise Exception('надо назначить имя сцене')



        self.x, self.y, self.width, self.height, self.parent = __args

        self.model.init_matrix()
        try:
            self.size_cell = self.width // len(self.model.matrix)
        except ZeroDivisionError:
            raise Exception('необходимо создать матрицу - поле')

    @property
    def user_style(self):
        return self._user_style

    @user_style.setter
    def user_style(self, style):
        print('chang_style {}'.format(style))
        self._user_style = style

    def _draw_ship(self, cell):
        self.ships[cell] = Item(QtGui.QPixmap(self.user_style.ship))
        self.ships[cell].setPos(*cell_to_coord(self.size_cell, cell))
        self.addItem(self.ships[cell])

    def _del_ship(self, cell):
        if cell in self.ships:
            self.removeItem(self.ships[cell])
            del(self.ships[cell])

    def accept_fleet(self):
        self.model.accept_fleet()

    def the_clear(self):
        self.model.clear_matrix()
        self.ships.clear()
        self.clear()


    def fire(self, cell):
        print('выстрелить по клетке')

    def do_nothing(self):
        print('нет действия')

    def build_ship(self, cell):
        print('построить корабль')
        y, x = cell
        self.model.matrix[y][x].tag = md.Cell.TagShip
        self.update_sea()

    def delite_ship(self, cell):
        print('удалить корабль')
        y, x = cell
        self.model.matrix[y][x].tag = md.Cell.StatusEmpty
        self.update_sea()

    def update_sea(self):
        self.clear()
        self.ships.clear()
        for line in self.model.matrix:
            for cell in line:
                if cell.tag == md.Cell.TagShip:
                    self._draw_ship(cell.coord)
                elif cell.tag == md.Cell.TagEmpty:
                    self._del_ship(cell.coord)


class View(QtWidgets.QGraphicsView):
    def __init__(self, *__args, size=None):
        super().__init__(*__args)
        self.setFixedSize(size, size)
        # self.scene = __args[0]
        self.parent = __args[1]

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.pos().x()
        y = QMouseEvent.pos().y()
        print(self.scene().size_cell)
        cell = coord_to_cell(self.scene().size_cell, y, x)
        if QMouseEvent.buttons() & QtCore.Qt.LeftButton:
            # координаты сцены преобразоваются в координаты модели
            self.parent.click_left_on_sea(self.scene(), cell)
        else:
            self.parent.click_right_on_sea(self.scene(), cell)


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
