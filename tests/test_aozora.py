import aozora
import pandas


def test_aozora_request():
    expect = pandas.DataFrame([
        {'term': 'し', 'info1': '動詞', 'info2': '自立', 'freq': 100},
        {'term': 'こと', 'info1': '名詞', 'info2': '非自立', 'freq': 93},
    ])

    a = aozora.AozoraTokenize()
    text = a.request(
        'https://www.aozora.gr.jp/cards/001428/files/50328_64360.html')
    text = a.extract(text)
    actual = a.freq(text).head(2).reset_index(drop=True)

    print(expect)
    print(actual)

    pandas.util.testing.assert_frame_equal(expect, actual)
