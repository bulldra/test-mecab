#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import argparse
import logzero
import settings
import MeCab
import pandas


class MecabTokenize:
    def __init__(self):
        logzero.logfile(
            settings.logfile,
            loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger
        self.mecab = MeCab.Tagger(settings.mecab_param)

    def tokenize(self, text):
        p = [li.split('\t') for li in self.mecab.parse(text).splitlines()]
        p = [[li[0]] + li[1].split('-') + [None] for li in p if len(li) == 2]
        p = [{'term': li[0], 'info1': li[1], 'info2': li[2]} for li in p]
        return pandas.DataFrame(p)

    def freq(self, text, groupby=['term', 'info1', 'info2']):
        s = self.tokenize(text).groupby(groupby).size()
        s = s.sort_values(ascending=False)
        return s.reset_index(name='freq')

    def term_freq(self, freq):
        all_freq = freq['freq'].sum()
        term_freq = freq['freq'].map(lambda freq: (freq / all_freq))
        df = pandas.DataFrame(freq)
        df['term_freq'] = term_freq
        return df

    def main(self, args):
        self.logger.info(f'{__file__} {__version__} {args}')
        term_list = self.tokenize(args.args1)
        print('単語品詞リスト')
        print(term_list)

        freq_list = self.freq(args.args1)
        print('\n単語出現リスト')
        print(freq_list)


if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        action='version', version=f'{__version__}'
    )
    parser.add_argument('args1')
    args = parser.parse_args()
    MecabTokenize().main(args)
