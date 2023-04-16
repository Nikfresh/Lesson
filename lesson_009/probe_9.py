# -*- coding: utf-8 -*-
import os
import zipfile
from pprint import pprint
from random import randint

# dirpath = 'python_snippets'
# zip_file_name = os.path.join(dirpath, 'voyna-i-mir.txt.zip')
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zfile.namelist():
#     print(filename)
#     zfile.extract(filename,path=dirpath)
# zfile.printdir()

dirpath = 'python_snippets'
filename = os.path.join(dirpath, 'voyna-i-mir.txt')
analize_count = 4

sequence = ' ' * analize_count
stat = {}
# stat = {'а':{'т':500,'x':300},'т':{'о':100,'у':50}}

with open(filename, 'r', encoding='cp1251') as file:
    for line in file:
        line = line[:-1]
        # print(line, end='')
        for char in line:
            if sequence in stat:
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence[1:] + char
# pprint(stat)
print(len(stat))

totals = {}
stat_for_gen = {}
for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_gen[sequence] = []
    for char, count in char_stat.items():
        totals[sequence] += count
        stat_for_gen[sequence].append([count, char])
    stat_for_gen[sequence].sort(reverse=True)
# print('TOTALS')
# pprint(totals)
# pprint(stat_for_gen)

N = 1000
printed = 0

sequence = ' ' * analize_count
spaces_printed = 0
while printed < N:
    char_stat = stat_for_gen[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    if char == ' ':
        spaces_printed += 1
        if spaces_printed >= 10:
            print()
            spaces_printed = 0
    printed += 1
    sequence = sequence[1:] + char
