# -*- coding: utf-8 -*-
import os
import zipfile

# dirpath = 'python_snippets'
# zip_file_name = os.path.join(dirpath, 'voyna-i-mir.txt.zip')
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zfile.namelist():
#     print(filename)
#     zfile.extract(filename,path=dirpath)
# zfile.printdir()

dirpath = 'python_snippets'
filename = os.path.join(dirpath, 'voyna-i-mir.txt')
prev_char = ' '
stat = {}
# stat = {'а':{'т':500,'x':300},'т':{'о':100,'у':50}}

with open(filename, 'r', encoding='cp1251') as file:
    for line in file:
        print(line, end='')
        for char in line:
            if prev_char in stat:
                if char in stat[prev_char]:
                    stat[prev_char][char] += 1
                else:
                    stat[prev_char][char] = 1
            else:
                stat[prev_char] = {char: 1}
