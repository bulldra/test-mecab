#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import argparse
import math
import logzero
import settings
import aozora


class AozoraTokenizeTfIdf:
    def __init__(self):
        logzero.logfile(
            settings.logfile,
            loglevel=20, maxBytes=1e6, backupCount=3
        )
        self.logger = logzero.logger
        self.aozora = aozora.AozoraTokenize()

    def execute(self, path):
        text = self.aozora.read(path)
        text = self.aozora.extract(text)
        freq = self.aozora.freq(text)
        return freq

    def main(self, args):
        self.logger.info(f'{__file__} {__version__} {args}')

        # TF作成
        target = self.execute(args.path)
        target = self.aozora.term_freq(target)

        # 全文書データ作成
        docs_path = [
            '../work/56645_58203.html',
            '../work/57105_59659.html',
            '../work/57181_59566.html',
            '../work/57240_60918.html',
            '../work/57849_71930.html',
        ]
        docs = None
        for path in docs_path:
            doc_freq = self.execute(path)
            doc_freq['doc_id'] = path
            if docs is None:
                docs = doc_freq
            else:
                docs = docs.append(doc_freq)

        # 単語・文書ID(path)でまとめる
        docs = docs.groupby(['term', 'doc_id']).sum()
        docs = docs.reset_index()

        # 単語出現文書数
        target['doc_freq'] = target['term'].map(
            lambda t: docs[docs['term'] == t].shape[0]
        )

        # IDF
        target['idf'] = target['doc_freq'].map(
            lambda t: math.log(len(docs_path) / t)
        )

        # tf-idf
        target['tf-idf'] = target['term_freq'] * target['idf']
        target = target.sort_values('tf-idf', ascending=False)

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
