#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import os
import json

def load_json(path):
    with open(_build_path(path), 'r') as conf:
        return json.load(conf)

def load_text(path):
    with open(_build_path(path), 'r') as conf:
        result = []
        for line in conf.read().splitlines():
            result.append(line)
        return result

def _build_path(path):
    abspath = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    abspath = os.path.abspath(abspath)
    if os.path.exists(abspath):
        return abspath
    else:
        raise FileNotFoundError(abspath)

settings_dict = load_json('../config/settings.json')
# secrets_dict = load_json('../config/secrets.json')
