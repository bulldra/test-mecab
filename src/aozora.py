#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import lxml.html
import lxml.html.clean
import requests
import mecab_tokenize


class AozoraTokenize:
    def __init__(self):
        self.mecab = mecab_tokenize.MecabTokenize()

    def request(self, url):
        res = requests.get(url)
        res.raise_for_status()
        res.encoding = 'shift_jis'
        return res.text.encode('shift_jis')

    def read(self, path):
        with open(path, 'r', encoding='shift_jis') as f:
            return f.read().encode('shift_jis')

    def extract(self, text):
        cleaner = lxml.html.clean.Cleaner(
            page_structure=False,
            remove_tags=['ruby', 'br'],
            kill_tags=['rt', 'rp']
        )
        html = cleaner.clean_html(text).decode('utf-8')
        html = lxml.html.fromstring(html)
        return html.find_class('main_text')[0].text_content()

    def freq(self, text, info=['名詞', '動詞']):
        df = self.mecab.freq(text)
        return df[df['info1'].isin(info)]

    def term_freq(self, freq):
        return self.mecab.term_freq(freq)
