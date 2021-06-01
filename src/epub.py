#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import argparse
import logzero
import settings
import ebooklib
from ebooklib import epub
import re
import mecab_tokenize


class EpubTokenize:
    def __init__(self):
        logzero.logfile(
            settings.logfile,
            loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger
        self.mecab = mecab_tokenize.MecabTokenize()

    def extract(self, path):
        text = ''
        for item in epub.read_epub(path).get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                text += re.sub(r'<.+?>', '', item.get_content().decode())
        return text

    def freq(self, text):
        df = self.mecab.freq(text)
        df = df[df['freq'] >= 10]
        df = df[df['info1'].isin(['名詞', '動詞']) & (df['term'].str.len() >= 2)]
        return df

    def main(self, args):
        self.logger.info(f'{__file__} {__version__} {args}')
        text = self.extract(args.path)
        df = self.freq(text)
        df.to_csv(args.path + '.freq', sep='\t')


if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        action='version', version=f'{__version__}'
    )
    parser.add_argument('path')
    args = parser.parse_args()
    EpubTokenize().main(args)
