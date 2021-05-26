#!/usr/bin/env python3
__version__ = "0.1.0"

import settings

def test_config():
    assert settings.settings_dict['logfile'] == '../log/info.log'

def test_load_json():
    settings_dict = settings.load_json('../config/settings.json')
    assert settings_dict['logfile'] == '../log/info.log'

def test_load_text():
    settings_list = settings.load_text('../config/settings.json')
    assert settings_list[0] == '{'
    assert settings_list[1] == '    "logfile" : "../log/info.log"'
    assert settings_list[2] == '}'

def test_build_path():
    path = settings._build_path('../config/settings.json')
    assert path == '/data/config/settings.json'

def test_notfilepath_list():
    try:
        settings.load_text('../config/settings.jso')
    except FileNotFoundError as e:
        assert str(e) == '/data/config/settings.jso'

def test_notfilepath_json():
    try:
        settings.load_json('../config/settings.jso')
    except FileNotFoundError as e:
        assert str(e) == '/data/config/settings.jso'
