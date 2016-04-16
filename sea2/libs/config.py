#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json


def config(path):
    with open(path, "r") as f:
        return json.load(f)



