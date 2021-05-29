#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import argparse
import logzero
import settings
import MeCab
import ebooklib
from ebooklib import epub
import re
import collections


class Main:
    def __init__(self):
        logzero.logfile(
            settings.logfile,
            loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger
        self.mecab = MeCab.Tagger(settings.mecab_param)

    def main(self, args):
        self.logger.info(f'{__file__} {__version__} {args}')
        book = epub.read_epub(args.args1)

        term_list = []
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                text = item.get_content().decode()
                text = re.sub(r'<.+?>', '', text)
                term_list += self.tokenize(text)
        d = {k: v for k, v in collections.Counter(
            term_list).items() if v >= 50}
        d = sorted(d.items(), key=lambda x: -x[1])
        print(d)

    def tokenize(self, text):
        p = [li.split('\t') for li in self.mecab.parse(text).splitlines()]
        p = [li[0] for li in p if len(li) == 2 and '名詞' in li[1]]
        return p


if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        action='version', version=f'{__version__}'
    )
    parser.add_argument('args1')
    args = parser.parse_args()
    Main().main(args)
