#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import mecab_tokenize
import collections


def test_tokenize1():
    text = '私はpythonでmecabを扱うテストをしています。'
    expect = [
        {'term': '私', 'pos': '名詞-代名詞-一般'},
        {'term': 'は', 'pos': '助詞-係助詞'},
        {'term': 'で', 'pos': '助詞-格助詞-一般'},
        {'term': 'mecab', 'pos': '名詞-固有名詞-一般'},
        {'term': 'を', 'pos': '助詞-格助詞-一般'},
        {'term': '扱う', 'pos': '動詞-自立'},
        {'term': 'テスト', 'pos': '名詞-サ変接続'},
        {'term': 'を', 'pos': '助詞-格助詞-一般'},
        {'term': 'し', 'pos': '動詞-自立'},
        {'term': 'て', 'pos': '助詞-接続助詞'},
        {'term': 'い', 'pos': '動詞-非自立'},
        {'term': 'ます', 'pos': '助動詞'},
        {'term': '。', 'pos': '記号-句点'},
    ]
    actual = mecab_tokenize.MecabTokenize().tokenize(text)
    assert(expect == actual)


def test_tokenize2():
    text = 'テストする'
    expect = [
        {'term': 'テスト', 'pos': '名詞-サ変接続'},
        {'term': 'する', 'pos': '動詞-自立'},
    ]
    actual = mecab_tokenize.MecabTokenize().tokenize(text)
    assert(expect == actual)


def test_freq():
    text = 'mecab mecabテストmecabテストツール'
    expect = collections.Counter(
        {'mecab': 3, 'テスト': 2, 'ツール': 1}
    )
    actual = mecab_tokenize.MecabTokenize().freq(text)
    assert(expect == actual)
