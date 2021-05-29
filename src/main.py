#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import argparse
import logzero
import settings
import MeCab


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
        term_list = self.tokenize(args.args1)
        print(term_list)

    def tokenize(self, text):
        p = [li.split('\t') for li in self.mecab.parse(text).splitlines()]
        return [{'term': li[0], 'pos': li[1]} for li in p if len(li) == 2]


if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        action='version', version=f'{__version__}'
    )
    parser.add_argument('args1')
    args = parser.parse_args()
    Main().main(args)
