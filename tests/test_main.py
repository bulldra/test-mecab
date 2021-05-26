#!/usr/bin/env python3
__version__ = "0.1.0"

import main

def test_main():
    assert main.Main().execute() == True
