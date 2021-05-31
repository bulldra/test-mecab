#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import lxml.html
import lxml.html.clean
import mecab_tokenize


class AozoraTokenize:
    def __init__(self):
        self.mecab = mecab_tokenize.MecabTokenize()

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

    def freq(self, text):
        df = self.mecab.freq(text)
        return df[df['info1'].isin(['名詞', '動詞']) & (df['term'].str.len() >= 2)]

    def term_freq(self, freq):
        return self.mecab.term_freq(freq)
