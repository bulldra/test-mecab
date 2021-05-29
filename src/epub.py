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

    def main(self, args):
        self.logger.info(f'{__file__} {__version__} {args}')
        book = epub.read_epub(args.args1)
        text = ''
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                text += re.sub(r'<.+?>', '', item.get_content().decode())
        print(mecab_tokenize.MecabTokenize().freq(text))


if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        action='version', version=f'{__version__}'
    )
    parser.add_argument('args1')
    args = parser.parse_args()
    EpubTokenize().main(args)
