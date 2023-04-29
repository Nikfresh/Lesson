# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import os
import time


class Organizing_photos:
    def __init__(self, scan_folder='E:\\foto_all', out_folder='E:\\foto_sorted'):
        self.scan_folder = scan_folder
        self.out_folder = out_folder

    def walk(self):
        for address, dirs, files in os.walk(self.scan_folder):
            for name in files:
                path = os.path.join(address, name)
                time = self.time_file(path)
                new_path = os.path.join(self.out_folder, str(time[0]), str(time[1]))
                # print(os.path.join(address, name),end=' ')
                # print('YEAR =',time[0], 'MONTH =', time[1],  'DAY =', time[2])
                self.copy_file(path,new_path)

    def time_file(self, path):
        secs = os.path.getmtime(path)
        return time.gmtime(secs)

    def copy_file(self, path,new_path):
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        shutil.copy2(path, new_path)


    # Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


org = Organizing_photos()
org.walk()
