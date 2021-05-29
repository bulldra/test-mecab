#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import argparse
import logzero
import settings
import MeCab
import pandas
import re
import collections


class KindleLib:
    def __init__(self):
        logzero.logfile(
            settings.settings_dict['logfile'],
            loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger
        self.mecab = MeCab.Tagger(settings.mecab_param)
        self.lib = pandas.read_csv(settings.kindle_lib_path, sep='\t')

    def main(self, args):
        self.logger.info(f'{__file__} {__version__} {args}')
        term_list = []
        s = self.lib.drop_duplicates(subset=['series_title'])
        for t in s['series_title']:
            term_list += self.execute(t)
        d = {k: v for k, v in collections.Counter(term_list).items() if v >= 5}
        d = sorted(d.items(), key=lambda x: -x[1])
        print(d)

    def execute(self, text):
        node = self.mecab.parseToNode(text)
        term_list = []
        while node:
            term = node.surface
            pos = node.feature.split(',')[0]
            if not re.match(r'^.{0,1}$', term) and pos in ['名詞', '動詞']:
                term_list.append(term)
            node = node.next
        return term_list


if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        action='version',
        version=f'{__version__}')
    args = parser.parse_args()
    KindleLib().main(args)
