# -*- coding: utf-8 -*-
import datetime
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
import zipfile


class Organizing_photos:
    def __init__(self, scan_folder='E:\\foto_all', out_folder='E:\\foto_sorted'):
        self.scan_folder = scan_folder
        self.out_folder = out_folder

    def walk(self):
        if self.scan_folder.endswith('.zip'):
            self.walk_zip()
            return
        for address, dirs, files in os.walk(self.scan_folder):
            for name in files:
                path = os.path.join(address, name)
                time = self.time_file(path)
                new_path = os.path.join(self.out_folder, str(time[0]), str(time[1]))
                # print(os.path.join(address, name),end=' ')
                # print('YEAR =',time[0], 'MONTH =', time[1],  'DAY =', time[2])
                self.copy_file(path, new_path)

    def time_file(self, path):
        secs = os.path.getmtime(path)
        return time.gmtime(secs)

    def copy_file(self, path, new_path):
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        shutil.copy2(path, new_path)

    def create_folder(self, new_path):
        if not os.path.isdir(new_path):
            os.makedirs(new_path)

    def walk_zip(self):
        with zipfile.ZipFile(self.scan_folder) as zf:
            for file in zf.infolist():
                date = datetime.datetime(*file.date_time)
                new_path = os.path.join(self.out_folder, str(date.year), str(date.month))
                name = os.path.basename(file.filename)
                if name:
                    old_name = os.path.join(file.filename)
                    file.filename = os.path.join(name)
                    self.create_folder(new_path)
                    zf.extract(file, new_path)
                    file.filename = old_name
                    file_path = os.path.join(new_path, name)
                    dat_w = datetime.datetime.strptime(f'{date.year}{date.month}{date.day}', '%Y%m%d').isoweekday()
                    m1 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
                    dat_day = m1[date.month - 1] + date.day

                    date_str = (date.year,date.month,date.day,date.hour,date.minute,date.second,dat_w,dat_day,-1)
                    new_mtime = new_atime = time.mktime(date_str)  # преобразует кортеж или struct_time в число секунд с начала эпохи. Обратная функция time.localtime.

                    os.utime(file_path, times=(new_atime, new_mtime))

    # Усложненное задание (делать по желанию)


# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


org = Organizing_photos(scan_folder='E:\\icons.zip')
org1 = Organizing_photos(out_folder='E:\\foto_sorted2')
org.walk()
org1.walk()
