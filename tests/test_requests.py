#!/usr/bin/env python3
__version__ = "0.1.0"

import requests

def test_requests():
    res = requests.get('https://raw.githubusercontent.com/bulldra/python-boilerplate/master/README.md')
    res.raise_for_status()
    assert res.status_code == 200

    with open('../work/README.md', 'wb') as f:
        for r in res.iter_content():
            f.write(r)
