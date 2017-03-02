#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json

cfg_path = '../etc/config.json'

def read_cfg(path):
    with open(path, "r") as f:
         return json.load(f)

def write_cfg(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4)

cfg = read_cfg(cfg_path)

class Config:
    _config = {}
    _config['tool_height'] = cfg['tool_height']
    _config['status_height'] = cfg['status_height']
    _config['ext'] = cfg['ext']
    _config['ext_icon'] = cfg['ext_icon']
    _config['default_style'] = cfg['default_style']
    _config['cell_size'] = cfg['cell_size']
    _config['count_cell'] = cfg['count_cell']
    _config['ship_names'] = cfg['ship_names']
    _config['actions_names'] = cfg['actions_names']

    @property
    def config(self):
        return self._config


    def set_config(self, opt, value):
        self._config[opt] = value

    def __getattr__(self, item):
        return self._config[item]

if __name__ == '__main__':
    c = Config()
    write_cfg('../etc/config.json', c.config)

