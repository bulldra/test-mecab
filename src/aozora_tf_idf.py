#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import argparse
import math
import logzero
import settings
import aozora
import glob
import pandas


class AozoraTokenizeTfIdf:
    def __init__(self):
        logzero.logfile(
            settings.logfile,
            loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger
        self.aozora = aozora.AozoraTokenize()

    def freq(self, path):
        text = self.aozora.extract(self.aozora.read(path))
        return self.aozora.freq(text, info=['名詞'])

    def docs_freq(self, docs_path):
        freq_list = []
        for path in docs_path:
            freq = self.freq(path)
            freq['doc_id'] = path
            freq_list.append(freq)

        # 単語・文書ID(path)でまとめる
        docs_freq = pandas.concat(freq_list)
        docs_freq = docs_freq.groupby(['term', 'doc_id']).sum()
        docs_freq = docs_freq.reset_index()
        return docs_freq

    def main(self, args):
        self.logger.info(f'{__file__} {__version__} {args}')

        # TF作成
        target = self.freq(args.path)
        target = self.aozora.term_freq(target)

        # 全文書データ作成
        docs_path = glob.glob('../work/*.html')
        docs_freq = self.docs_freq(docs_path)

        # 単語出現文書数
        target['doc_freq'] = target['term'].map(
            lambda t: (docs_freq['term'] == t).sum()
        )

        # IDF
        doc_num = len(docs_path)
        target['idf'] = target['doc_freq'].map(
            lambda df: math.log(doc_num / df)
        )

        # tf-idf
        target['tf-idf'] = target['term_freq'] * target['idf']
        target = target.sort_values('tf-idf', ascending=True)
        target = target.tail(20)
        target = target.reset_index(drop=True)

        # ファイル出力
        out_path = args.path + '.tsv'
        target.to_csv(out_path, sep='\t')


if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        action='version', version=f'{__version__}'
    )
    parser.add_argument('path')
    args = parser.parse_args()
    AozoraTokenizeTfIdf().main(args)
