import ebooklib
from ebooklib import epub

book = epub.read_epub('work/oreilly-978-4-87311-778-2e.epub')

title = book.get_metadata('DC', 'title')
creator = book.get_metadata('DC', 'creator')
publisher = book.get_metadata('DC', 'publisher')
language = book.get_metadata('DC', 'language')

print(title)  # タイトル
print(creator)  # 執筆者
print(publisher)  # 発行人
print(language)  # 言語

items = book.get_items()
for item in items:
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        print('==================================')
        print('ファイル名 : ', item.get_name())  # ファイル名
        print('==================================')
        print(item.get_content().decode()[0:2000])  # 本文をファイルごとに書き出し
        print('==================================')
