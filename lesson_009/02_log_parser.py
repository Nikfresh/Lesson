# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Analizer_log:

    def __init__(self, file_name):
        self.file_name_read = file_name
        self.file_name_save = 'out_stat_time.txt'
        self.old_str = ''
        self.new_str = ''
        self.quant = 0

    def __str__(self):
        return

    def go_stat(self):
        with open(self.file_name_read, 'r', encoding='utf8') as file_r:
            for line in file_r:
                self._counter(line=line)

    def writer(self):
        if self.old_str:
            string = f'{self.old_str}] {self.quant}\n'
            with open(self.file_name_save, 'a', encoding='utf8') as file_w:
                file_w.write(string)

    def _counter(self, line):
        self.new_str = line[:17]
        if self.new_str > self.old_str:
            self.writer()
            self.old_str = self.new_str
            self.quant = 0
            return
        elif 'NOK' in line:
            self.quant+=1
            return


log= Analizer_log(file_name='events.txt')
log.go_stat()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
