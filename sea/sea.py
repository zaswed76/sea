#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Cell:
    _max = 9
    _min = 0
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.shooting = False  # стреляли ли в эту клетку
        self._distance_to_obstacles_x = self._max - (self.x - 1)
        self._distance_to_obstacles_y = self._max - (self.y - 1)

    @property
    def distance_to_obstacles_x(self):
        return self._distance_to_obstacles_x

    @distance_to_obstacles_x.setter
    def distance_to_obstacles_x(self, obstacles):
        self._distance_to_obstacles_x = self._max - (obstacles - 1)

    @property
    def distance_to_obstacles_y(self):
        return self._distance_to_obstacles_y

    @distance_to_obstacles_y.setter
    def distance_to_obstacles_y(self, obstacles):
        self._distance_to_obstacles_y = self._max - (obstacles - 1)

    def __repr__(self):
        return '({}, {})'.format(self.y, self.x)


class Sea(list):
    def __init__(self):
        super().__init__()


    def create_field(self, width, height):
        for y in range(height):
            line = []
            for x in range(width):
                line.append((Cell(x, y)))
            self.append(line)

class Ship(list):
    Vertical = 1
    Horizontal = 0
    def __init__(self, bow, course, deck):
        super().__init__()
        self.x, self.y = bow
        self.course = course
        self.deck = deck
        self.corpus = self._set_corpus()
        self._around = []

    def _set_corpus(self):
        if self.course == self.Horizontal:
            return [(self.x + n, self.y) for n in range(self.deck)]
        else:
            return [(self.x, self.y + n) for n in range(self.deck)]


    def _set_around(self):
        pass




if __name__ == '__main__':
    s = Ship((1, 1), Ship.Horizontal, 2)
    print(s.corpus)

