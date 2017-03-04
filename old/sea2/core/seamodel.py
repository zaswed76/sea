#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy

LIMIT_MAX = 9
LIMIT_MIN = 0


class Cell:
    TagEmpty = 'empty'
    TagShip = 'ship'
    TagHurt = 'hurt'
    TagShot = 'shot'
    TagBordure = 'bordure'
    TagNames = ['empty', 'ship', 'hurt', 'shot', 'bordure']
    ListBusy = ['ship', 'hurt', 'shot', 'bordure']
    ListEmpty = ['empty']
    StatusBusy = 'busy'
    StatusEmpty = 'empty'

    def __init__(self, y, x):
        super().__init__()
        self.x = x
        self.y = y
        self.coord = (self.y, self.x)
        self._tag = Cell.TagEmpty
        self._status = Cell.StatusEmpty

    @property
    def tag(self):
        return self._tag

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, tag):
        if tag in Cell.ListBusy:
            self._status = Cell.StatusBusy
        else:
            self._status = Cell.StatusEmpty

    @tag.setter
    def tag(self, tag):
        if tag in Cell.TagNames:
            self._tag = tag
            self.status = tag

        else:
            raise Exception('not_name tag')

    def __repr__(self):
        return str(Cell.TagNames.index(self.tag))


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
        self.y, self.x = bow
        self.course = course
        self.deck = deck
        self.name = name
        self.max = LIMIT_MAX + 1
        self.min = LIMIT_MIN - 1
        self.init_ship()

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

    def init_ship(self):
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

    def __contains__(self, item):
        for ship in self.values():
            if item in ship:
                return True
        else:
            return False


class Sea:
    min = 0
    max = 9

    def __init__(self, fleet):
        self.fleet = fleet
        self.matrix = []

    def __getitem__(self, item):
        return self.matrix[item]

    def add_ship(self, name, ship):
        self.fleet[name] = ship

    def build_ship(self, cell):
        ''' построить корабль '''
        y, x = cell
        self.matrix[y][x].tag = Cell.TagShip


    def init_matrix(self):
        self.matrix.clear()
        _range = range(self.max + 1)
        for y in _range:
            self.matrix.append([Cell(y, x) for x in _range])

    def clear_matrix(self):
        for line in self.matrix:
            for cell in line:
                cell.tag = Cell.TagEmpty

    def build_composite_ship(self, bow, course, deck):
        y, x = bow
        if course == Ship.Horizontal:
            for n in range(deck):
                pass


    def accept_fleet(self):
        for line in self.matrix:
            for cell in line:
                # клетка уже является частью флота
                if cell in self.fleet:
                    continue
                # если является кораблём
                if cell.tag == Cell.TagShip:
                    # искать корабль справа
                    h_deck = self._search_horizontal_ship(cell.coord)




    def _search_horizontal_ship(self, coord):
        deck = 0
        y, x = coord
        while x != self.max:
            x += 1
            if self.matrix[y][x].tag == Cell.TagShip:
                deck += 1
                continue
        return deck

    def __str__(self):
        return str(numpy.array(self.matrix))


if __name__ == '__main__':
    sea = Sea(Fleet)
    sea.init_matrix()

    sea[0][0].tag = Cell.TagShip
    print(sea[0][0].coord)
