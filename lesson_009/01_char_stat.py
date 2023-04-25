# -*- coding: utf-8 -*-
from pprint import pprint


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Statistic_creator:

    def __init__(self, file_name):
        self.file_name = file_name
        self.base_stat = {}
        self.stat_abc = []
        self.stat_123 = []

    def __str__(self):
        return self.base_stat

    def print_stat(self):
        pprint(self.base_stat)

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            print(filename)
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()

        self.base_stat = {}
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])
        # pprint(stat)
        print(len(self.base_stat))

    def _collect_for_line(self, line):
        for char in line:
            status_char = char.isalpha()
            if status_char:
                if char in self.base_stat:
                    self.base_stat[char] += 1
                else:
                    self.base_stat[char] = 1

    def print_stat_abs_up(self):
        self._prepare_abs()
        self.stat_abc.sort()
        self._print_stat()

    def print_stat_abs_down(self):
        self._prepare_abs()
        self.stat_abc.sort(reverse=True)
        self._print_stat()

    def print_stat_123_up(self):
        self._prepare_123()
        self.stat_abc.sort(reverse=True)
        for char, quant in self.stat_abc.items():
        self.stat_abc = [char, quant]
        self._print_stat()

    def print_stat_123_down(self):
        self._prepare_123()
        self.stat_abc.sort()
        self._print_stat()

    def _print_stat(self):
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for char, quant in self.stat_abc:
            print(f'|{char:^9}|{quant:^10}|')

    def _prepare_abs(self):
        self.stat_abc = []
        for char, quant in self.base_stat.items():
            self.stat_abc.append([char, quant])
        # pprint(self.stat_abc)

    def _prepare_123(self):
        self.stat_abc = []
        for char, quant in self.base_stat.items():
            self.stat_abc.append([quant, char])


analise = Statistic_creator(file_name='voyna-i-mir.txt')
analise.collect()
analise.print_stat()
analise.print_stat_123_up()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
