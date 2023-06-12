# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


class Analizer_log:

    def __init__(self, file_name):
        self.ferst_line = 1
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
        if self.ferst_line == 1:
            self.old_str = line[:17]
            self.ferst_line = 0
        self.new_str = line[:17]
        if self.new_str > self.old_str:
            self.writer()
            self.old_str = self.new_str
            self.quant = 0
            return
        elif 'NOK' in line:
            self.quant += 1
            return

    def __iter__(self):
        # обнуляем счетчик перед циклом
        self.ferst_line = 1
        self.old_str = ''
        self.new_str = ''
        self.quant = 0
        self.file_r = open(self.file_name_read, 'r', encoding='utf8')
        # возвращаем ссылку на себя - я буду итератором!
        return self

    def __next__(self):
        for line in self.file_r:

            if self.ferst_line == 1:
                self.old_str = line[:17]
                self.ferst_line = 0
            self.new_str = line[:17]
            if self.new_str > self.old_str:
                self.res = str(self.old_str), str(self.quant)
                self.old_str = self.new_str
                if 'NOK' in line:
                    self.quant = 1
                else: self.quant = 0

                # print(file_r.tell())
                return self.res
            elif 'NOK' in line:
                self.quant += 1
        if self.quant > 0:
            self.res = str(self.old_str), str(self.quant)
            self.quant = 0
            return self.res
        self.file_r.close()
        raise StopIteration()  # признак того, что больше возвращать нечего


# log= Analizer_log(file_name='events.txt')
# log.go_stat()

grouped_events = Analizer_log(file_name='events.txt')
for group_time, event_count in grouped_events:
    print(f'{group_time}] {event_count}')
