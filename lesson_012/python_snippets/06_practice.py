# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib.request import urlopen

# Задача: проверить у какого сайта "тяжелее" главная страница.
# - получить html
# - узнать какие CSS и JS файлы нужны для отображения
# - подсчитать общий размер этих файлов
# - вывести на консоль результаты

sites = [
    # 'https://www.fl.ru',
    # 'https://stepik.org/',
    'https://www.freelancejob.ru/',
    'https://kwork.ru',
    'https://mega.io/',
    'https://www.all-light-media.ru/',
]


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'link':
            return
        print("Start tag:", tag,flush=True)
        for attr in attrs:
            print("     attr:", attr,flush=True)


for url in sites:
    res = urlopen(url)
    html_data = res.read()
    html_data = html_data.decode('utf-8')
    total_bytes = len(html_data)
    parser = MyHTMLParser()
    parser.feed(html_data)

'''
import requests

from extractor import LinkExtractor
from utils import time_track




class PageSizer:

    def __init__(self, url):
        self.url = url
        self.total_bytes = 0

    def run(self):
        self.total_bytes = 0
        html_data = self._get_html(url=self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        extractor = LinkExtractor(base_url=self.url)
        extractor.feed(html_data)
        for link in extractor.links:
            extra_data = self._get_html(url=link)
            if extra_data:
                self.total_bytes += len(extra_data)

    def _get_html(self, url):
        try:
            print(f'Go {url}...')
            res = requests.get(url)
        except Exception as exc:
            print(exc)
        else:
            return res.text


@time_track
def main():
    sizers = [PageSizer(url=url) for url in sites]

    for sizer in sizers:
        sizer.run()

    for sizer in sizers:
        print(f'For url {sizer.url} need download {sizer.total_bytes//1024} Kb ({sizer.total_bytes} bytes)')


if __name__ == '__main__':
    main()
'''
