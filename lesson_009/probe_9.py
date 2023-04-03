# -*- coding: utf-8 -*-
import os
import zipfile

dirpath = 'D:\phython_prog_lesson\lesson_009\python_snippets'
zip_file_name = os.path.join(dirpath, 'voyna-i-mir.txt.zip')
zfile = zipfile.ZipFile(zip_file_name, 'r')
for filename in zfile.namelist():
    print(filename)
    zfile.extract(filename,path=dirpath)
zfile.printdir()