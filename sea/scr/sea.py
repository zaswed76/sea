#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Config:
    size = 10
    max = size - 1
    min = 0
    complexity = 0

    def set_size(self, s):
        self.size = s

    def set_complexity(self, c):
        self.complexity = c

    def horizontal_lock(self):
        lst = []
        for y in range(self.min + 1, self.max):
            lst.extend([(x, y) for x in range(self.min, self.size)])
        return lst

    def vertical_lock(self):
        lst = []
        for y in range(self.min, self.size):
            lst.extend(
                    [(x, y) for x in range(self.min + 1, self.max)])
        return lst


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
        self.reset()

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

    def reset(self):
        self.horizontal_lock = False
        self.vertical_lock = False
        self.shooting = False  # стреляли ли в эту клетку
        self.ship_place = False  # размещает ли корабль весь
        self._distance_to_obstacles_x = Config.max - (self.x - 1)
        self._distance_to_obstacles_y = Config.max - (self.y - 1)

    def __repr__(self):
        return 'Cell - ({}, {})'.format(self.x, self.y)

class Ship(list):
    Vertical = 'vertical'
    Horizontal = 'horizontal'
    Left_beacon = 'left_beacon'
    Top_beacon = 'top_beacon'
    StatusFull = 'full'
    StatusWounded = 'wounded'
    StatusKill = 'kill'

    def __init__(self, bow, course, deck, name):
        super().__init__()
        self.name = name
        self.bow = bow
        self.max = Config.max + 1
        self.min = Config.min - 1
        self.x, self.y = bow
        self.course = course
        self.deck = deck
        self._status = Ship.StatusFull
        self.corpus = []
        self.around = []
        self.top_beacon = []
        self.left_beacon = []
        self.set_ship()

    def wound(self, value):
        self.corpus.remove(value)
        self.update_status()

    @property
    def status(self):
        return self._status

    def update_status(self):
        if not self.corpus:
            self._status = Ship.StatusKill
        elif len(self.corpus) < self.deck:
            self._status = Ship.StatusWounded
        else:
            self._status = Ship.StatusFull

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


class Fleet(dict):
    def __init__(self):
        super().__init__()

    def add_ship(self, name, ship):
        self[name] = ship

    def ships_coord(self):
        lst = []
        for ship in self.values():
            lst.append(ship.corpus)
        return lst

    def shot(self, item):
        for name in self:
            ship = self[name]
            if item in ship.corpus:
                ship.wound(item)

                return (True, ship.status, ship.name)
        else:
            return (False, None, None)

    def __contains__(self, item):
        for ship in self.values():
            if item in ship:
                return True
        else:
            return False


class Sea(dict):
    def __init__(self, ship_names):
        super().__init__()
        self.ship_names = ship_names
        self.fleet = Fleet()

    def create_field(self):
        for y in range(Config.size):
            for x in range(Config.size):
                self[(x, y)] = Cell(x, y)

    def reset(self):
        for cell in self.values():
            cell.reset()
            if (cell.x, cell.y) in Config.horizontal_lock(Config):
                cell.horizontal_lock = True
            if (cell.x, cell.y) in Config.vertical_lock(Config):
                cell.vertical_lock = True

    @property
    def empty(self):
        return [c for c in self.values() if not c.ship_place]

    def _reg_horizontal(self, cell, deck):
        if deck > 1 and cell.horizontal_lock:
            return False
        if cell.distance_to_obstacles_x >= deck and not cell.ship_place:
            return True

    def _reg_vertical(self, cell, deck):
        if deck > 1 and cell.vertical_lock:
            return False
        if cell.distance_to_obstacles_y >= deck and not cell.ship_place:
            return True

    def permissible(self, course, deck):
        permissible = []
        for cell in self.values():
            if course == Ship.Horizontal:
                if self._reg_horizontal(cell, deck):
                    permissible.append(cell)
            else:
                if self._reg_vertical(cell, deck):
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
            if nx < Config.min:  # конец поля
                return
            if (nx, y) in self.fleet:  # уткнулись в корабль
                return
            self[(nx, y)].distance_to_obstacles_x = x

    def _scan_to_top(self, x, y, seq):
        for n in seq:
            ny = y + n
            if ny < Config.min:  # конец поля
                return
            if (x, ny) in self.fleet:  # уткнулись в корабль
                return
            self[(x, ny)].distance_to_obstacles_y = y

    def create_fleet(self):
        while True:
            self.fleet.clear()
            self.reset()
            for name, deck in enumerate(self.ship_names):
                # направление
                course = random.choice(
                        [Ship.Vertical, Ship.Horizontal])

                perm = self.permissible(course, deck)
                try:
                    bow = random.choice(perm)
                except IndexError:
                    continue
                ship = Ship(bow, course, deck, name)
                self.add_ship(name, ship)
                self.update_cells(ship)

            if len(self.empty) > Config.complexity:
                break




if __name__ == '__main__':
    s = Sea()
