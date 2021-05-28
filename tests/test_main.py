#!/usr/bin/env python3
__version__ = "0.1.0"

import main

def test_main():
    expect = [
        {'term': '', 'pos': 'BOS/EOS'},
        {'term': '私', 'pos': '名詞'},
        {'term': 'は', 'pos': '助詞'},
        {'term': 'python', 'pos': '名詞'},
        {'term': 'で', 'pos': '助詞'},
        {'term': 'mecab', 'pos': '名詞'},
        {'term': 'を', 'pos': '助詞'},
        {'term': '扱う', 'pos': '動詞'},
        {'term': 'テスト', 'pos': '名詞'},
        {'term': 'を', 'pos': '助詞'},
        {'term': 'し', 'pos': '動詞'},
        {'term': 'て', 'pos': '助詞'},
        {'term': 'い', 'pos': '動詞'},
        {'term': 'ます', 'pos': '助動詞'},
        {'term': '。', 'pos': '記号'},
        {'term': '', 'pos': 'BOS/EOS'}]
    actual = main.Main().execute('私はpythonでmecabを扱うテストをしています。')
    assert expect == actual
