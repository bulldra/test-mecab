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
            settings.settings_dict['logfile'],
            loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger
        self.mecab = MeCab.Tagger('-d /usr/local/etc/mecab-ipadic-neologd')

    def main(self, args):
        self.logger.info(f'{__file__} {__version__} {args}')
        term_list = self.execute(args.args1)
        print(term_list)

    def execute(self, text):
        node = self.mecab.parseToNode(text)
        term_list = []
        while node:
            term_list.append({
                'term': node.surface,
                'pos': node.feature.split(',')[0]
            })
            node = node.next
        return term_list

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=f'{__version__}')
    parser.add_argument('args1')
    args = parser.parse_args()
    Main().main(args)
