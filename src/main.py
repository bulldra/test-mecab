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
        self.mecab = MeCab.Tagger()

    def main(self, args):
        self.logger.info(f'{__file__} {__version__} {args}')
        self.execute(args.args1)

    def execute(self, text):
        node = self.mecab.parseToNode(text)
        while node:
            word = node.surface
            pos = node.feature.split(',')[1]
            print(f'{word}, {pos}')
            node = node.next

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=f'{__version__}')
    parser.add_argument('args1')
    args = parser.parse_args()
    Main().main(args)
