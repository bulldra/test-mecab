#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import argparse
import logzero
import settings
import MeCab
import collections


class MecabTokenize:
    def __init__(self):
        logzero.logfile(
            settings.logfile,
            loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger
        self.mecab = MeCab.Tagger(settings.mecab_param)

    def main(self, args):
        self.logger.info(f'{__file__} {__version__} {args}')
        term_list = self.tokenize(args.args1)
        print('単語品詞リスト')
        print(term_list)

        freq_list = self.freq(args.args1)
        print('\n単語出現リスト')
        print(freq_list)

    def tokenize(self, text):
        p = [li.split('\t') for li in self.mecab.parse(text).splitlines()]
        return [{'term': li[0], 'pos': li[1]} for li in p if len(li) == 2]

    def freq(self, text):
        return collections.Counter([t['term'] for t in self.tokenize(text)])


if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        action='version', version=f'{__version__}'
    )
    parser.add_argument('args1')
    args = parser.parse_args()
    MecabTokenize().main(args)
