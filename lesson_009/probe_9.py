# -*- coding: utf-8 -*-
import os
import zipfile
from pprint import pprint
from random import randint


class Chatter:
    analize_count = 4

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):

        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            print(filename)
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        self.sequence = ' ' * self.analize_count
        stat = {}
        # stat = {'а':{'т':500,'x':300},'т':{'о':100,'у':50}}

        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line = line[:-1])
        # pprint(stat)
        print(len(self.stat))

    def _collect_for_line(self, line):
        for char in line:
            if self.sequence in self.stat:
                if char in self.stat[self.sequence]:
                    self.stat[self.sequence][char] += 1
                else:
                    self.stat[self.sequence][char] = 1
            else:
                self.stat[self.sequence] = {char: 1}
            self.sequence = self.sequence[1:] + char

    def prepare(self):
        self.totals = {}
        self.stat_for_gen = {}
        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_gen[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_gen[sequence].append([count, char])
            self.stat_for_gen[sequence].sort(reverse=True)

    def chat(self, N, ouf_file_name = None):
        N = 1000
        printed = 0
        if ouf_file_name is not None:
            file = open(ouf_file_name,'w',encoding='utf8')
        else:
            file = None

        sequence = ' ' * self.analize_count
        spaces_printed = 0
        while printed < N:
            char_stat = self.stat_for_gen[sequence]
            total = self.totals[sequence]
            char = self._get_char(char_stat, total)
            if file:
                file.write(char)
            else:
                print(char, end='')
            if char == ' ':
                spaces_printed += 1
                if spaces_printed >= 10:
                    if file:
                        file.write('\n')
                    else:
                        print()
                    spaces_printed = 0
            printed += 1
            sequence = sequence[1:] + char
        if file :
            file.close()

    def _get_char(self, char_stat, total):
        dice = randint(1, total)
        pos = 0
        for count, char in char_stat:
            pos += count
            if dice <= pos:
                break
        return char


file_name = 'voyna-i-mir.txt'
chatterer = Chatter(file_name=file_name)
chatterer.collect()
chatterer.prepare()
chatterer.chat(N=100,ouf_file_name='out.txt')
