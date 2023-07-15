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


class LinkExtraktor(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag not in ('link','script',):
            return
        attrs = dict(attrs)
        if tag == 'link':
            if 'rel' in attrs and attrs['rel'] == 'stylesheet' and 'href' in attrs:
                print('find  href',attrs['rel'],'_________',attrs['href'])
                self.links.append(attrs['href'])
            if 'rel' in attrs and attrs['rel'] == 'stylesheet' and 'data-href' in attrs:
                print('find_______data-href',attrs['rel'],'_________',attrs['data-href'])
                self.links.append(attrs['data-href'])
        elif tag == 'script':
            if 'src' in attrs :
                print('find  src',attrs['src'],'__^^^^^^^^^^___',attrs['src'])
                self.links.append(attrs['src'])

for url in sites:
    res = urlopen(url)
    html_data = res.read()
    html_data = html_data.decode('ISO-8859–1')
    total_bytes = len(html_data)
    extraktor = LinkExtraktor()
    extraktor.feed(html_data)
    print(extraktor.links)
    for link in extraktor.links:
        res = urlopen(link)
        extra_data = res.read()
        extra_data = extra_data.decode('ISO-8859–1')
        total_bytes = len(extra_data)

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
