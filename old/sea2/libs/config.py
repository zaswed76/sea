#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json



def read_cfg(path):
    with open(path, "r") as f:
         return json.load(f)

def write_cfg(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4)



