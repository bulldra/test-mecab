#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import mecab_tokenize
import pandas


def test_tokenize1():
    text = 'テストする'
    expect = pandas.DataFrame([
        {'term': 'テスト', 'info1': '名詞', 'info2': 'サ変接続'},
        {'term': 'する', 'info1': '動詞', 'info2': '自立'},
    ])
    actual = mecab_tokenize.MecabTokenize().tokenize(text)
    pandas.util.testing.assert_frame_equal(expect, actual)


def test_tokenize2():
    text = 'mecab mecabテストmecabテストツール'
    expect = pandas.DataFrame([
        {'term': 'mecab', 'info1': '名詞', 'info2': '固有名詞'},
        {'term': 'mecab', 'info1': '名詞', 'info2': '固有名詞'},
        {'term': 'テスト', 'info1': '名詞', 'info2': 'サ変接続'},
        {'term': 'mecab', 'info1': '名詞', 'info2': '固有名詞'},
        {'term': 'テスト', 'info1': '名詞', 'info2': 'サ変接続'},
        {'term': 'ツール', 'info1': '名詞', 'info2': '一般'},
    ])
    actual = mecab_tokenize.MecabTokenize().tokenize(text)
    pandas.util.testing.assert_frame_equal(expect, actual)


def test_freq():
    text = 'mecab mecabテストmecabテストツール'
    expect = pandas.DataFrame([
        {'term': 'mecab', 'info1': '名詞', 'info2': '固有名詞', 'freq': 3},
        {'term': 'テスト', 'info1': '名詞', 'info2': 'サ変接続', 'freq': 2},
        {'term': 'ツール', 'info1': '名詞', 'info2': '一般', 'freq': 1},
    ])
    actual = mecab_tokenize.MecabTokenize().freq(text)
    pandas.util.testing.assert_frame_equal(expect, actual)
