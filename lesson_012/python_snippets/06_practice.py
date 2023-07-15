# -*- coding: utf-8 -*-

import requests

from extractor import LinkExtractor
from utils import time_track

# Задача: проверить у какого сайта "тяжелее" главная страница.
# - получить html
# - узнать какие CSS и JS файлы нужны для отображения
# - подсчитать общий размер этих файлов
# - вывести на консоль результаты

sites = [
    'https://www.fl.ru',
    'https://www.weblancer.net/',
    'https://www.freelancejob.ru/',
    'https://kwork.ru',
    'https://work-zilla.com/',
    'https://iklife.ru/udalennaya-rabota-i-frilans/poisk-raboty/vse-samye-luchshie-sajty-i-birzhi-v-internete.html',
]


class PageSizer:
    def __init__(self,url):
        self.url = url
        self.total_bytes = 0

    def run(self):
        self.total_bytes = 0
        html_data = self._get_html(url=self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        extraktor = LinkExtractor(base_url=self.url)
        extraktor.feed(html_data)
        for link in extraktor.links:
            extra_data = self._get_html(url=link)
            if extra_data :
                self.total_bytes += len(extra_data)
        pass
    def _get_html(self,url):
        try:
            print(f'Go {url}...')
            res = requests.get(url)
        except Exception as exc:
            print(exc)
            return
        else:
            return res.text

@time_track
def main():
    sizers = [PageSizer(url=url) for url in sites]
    for sizer in sizers:
        sizer.run()
    for sizer in sizers:
        print(f'For url {sizer.url} need download {sizer.total_bytes / 1024} Kb')

if __name__ == '__main__':
    main()

