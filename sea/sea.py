#!/usr/bin/env python
# -*- coding: utf-8 -*-


_max = 9
_min = 0

class SeaError(Exception): pass

side_error_message = '''стороны могут быть:
'left_beacon' ; Ship.Left_beacon
'top_beacon' ; Ship.Top_beacon '''

class Cell(list):
    def __init__(self, x, y):
        super().__init__()
        self.extend([x, y])
        self.y = y
        self.x = x
        self.shooting = False  # стреляли ли в эту клетку
        self.ship_place = False  # размещает ли корабль
        self._distance_to_obstacles_x = _max - (self.x - 1)
        self._distance_to_obstacles_y = _max - (self.y - 1)

    @property
    def distance_to_obstacles_x(self):
        return self._distance_to_obstacles_x

    @distance_to_obstacles_x.setter
    def distance_to_obstacles_x(self, obstacles):
        self._distance_to_obstacles_x = obstacles - self.x

    @property
    def distance_to_obstacles_y(self):
        return self._distance_to_obstacles_y

    @distance_to_obstacles_y.setter
    def distance_to_obstacles_y(self, obstacles):
        self._distance_to_obstacles_y = obstacles - self.y

    def __repr__(self):
        return 'Cell - ({}, {})'.format(self.x, self.y)


class Fleet(dict):
    def __init__(self):
        super().__init__()

    def add_ship(self, name, ship):
        self[name] = ship

    def __contains__(self, item):
        for ship in self.values():
            if item in ship:
                return True
        else:
            return False




class Sea(dict):
    def __init__(self):
        super().__init__()
        self.fleet = None

    def set_fleet(self, fleet):
        self.fleet = fleet

    def create_field(self, width, height):
        for y in range(height):
            for x in range(width):
                self[(x, y)] = Cell(x, y)

    def permissible(self, course, deck):
        permissible = []
        for cell in self.values():
            if course == Ship.Horizontal:
                if cell.distance_to_obstacles_x >= deck and not cell.ship_place:
                    permissible.append(cell)
            else:
                if cell.distance_to_obstacles_y >= deck and not cell.ship_place:
                    permissible.append(cell)
        return permissible

    def add_ship(self, name, ship):
        self.fleet[name] = ship

    def update_cells(self, ship):

        """

        :param ship: list < tuple
        """
        # клетка занята кораблём
        back_seq = range(-1, -5, -1)
        for cell in ship:
            self[cell].ship_place = True

        # обновляем
        for x, y in ship.left_beacon:
            self._scan_to_left(x, y, back_seq)
        for x, y in ship.top_beacon:
            self._scan_to_top(x, y, back_seq)


    def _scan_to_left(self, x, y, seq):
            for n in seq:
                nx = x + n
                if nx < _min: # конец поля
                    return
                if (nx, y) in self.fleet: # уткнулись в корабль
                    return
                self[(nx, y)].distance_to_obstacles_x = x

    def _scan_to_top(self, x, y, seq):
            for n in seq:
                ny = y + n
                if ny < _min: # конец поля
                    return
                if (x, ny) in self.fleet: # уткнулись в корабль
                    return
                self[(x, ny)].distance_to_obstacles_y = y




class Ship(list):
    Vertical = 'vertical'
    Horizontal = 'horizontal'
    Left_beacon = 'left_beacon'
    Top_beacon = 'top_beacon'

    def __init__(self, bow, course, deck):
        super().__init__()
        self.max = _max + 1
        self.min = _min - 1
        self.x, self.y = bow
        self.course = course
        self.deck = deck
        self.corpus = []
        self.around = []
        self.top_beacon = []
        self.left_beacon = []
        self.set_ship()

    def _border_filter(self, x, y):
        return self.min < x < self.max and self.min < y < self.max

    def _around_hor(self):
        res = []
        top_y = self.y - 1
        bottom_y = self.y + 1
        left = (self.x - 1, self.y)
        right = (self.x + self.deck, self.y)
        top = [(self.x + n, top_y) for n in range(-1, self.deck + 1)]
        bot = [(self.x + n, bottom_y) for n in
               range(-1, self.deck + 1)]

        res.append(left)
        res.append(right)
        res.extend(top)
        res.extend(bot)
        return [(x, y) for x, y in res if self._border_filter(x, y)]

    def _around_ver(self):
        res = []
        left_x = self.x - 1
        right_x = self.x + 1
        top = (self.x, self.y - 1)
        bottom = (self.x, self.y + self.deck)
        left = [(left_x, self.y + n) for n in
                range(-1, self.deck + 1)]
        right = [(right_x, self.y + n) for n in
                 range(-1, self.deck + 1)]
        res.append(top)
        res.append(bottom)
        res.extend(left)
        res.extend(right)
        return [(x, y) for x, y in res if self._border_filter(x, y)]

    def set_ship(self):
        if self.course == self.Horizontal:
            self.corpus = [(self.x + n, self.y) for n in
                           range(self.deck)]
            self.around = self._around_hor()
            self.extend(self.corpus + self.around)
        else:
            self.corpus = [(self.x, self.y + n) for n in
                           range(self.deck)]
            self.around = self._around_ver()
            self.extend(self.corpus + self.around)
        self.top_beacon = self.set_top_beacon
        self.left_beacon = self.set_left_beacon

    @property
    def set_top_beacon(self):
        ty = self.y - 1
        return [(x, y) for x, y in self if y == ty]

    @property
    def set_left_beacon(self):
        tx = self.x - 1
        return [(x, y) for x, y in self if x == tx]


if __name__ == '__main__':
    s = Sea()
    s.create_field(10, 10)
    s.set_permissible(Ship.Horizontal, 4)
    print(s.permissible)
