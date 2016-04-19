#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Model:
    def __init__(self):
        self.x = 1

class Scene:
    def __init__(self, model):
        self.model = model
        self.s = 0

    def update(self):
        self.s = self.model.x






class Main:
    def __init__(self):
        self.model = Model()
        self.scene = Scene(self.model)