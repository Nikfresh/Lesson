# -*- coding: utf-8 -*-
from datetime import datetime


# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class Analise_reg():

    def __int__(self, file='registrations.txt'):
        self.good_log = 'registrations_good.log'
        self.bad_log = 'registrations_bad.log'
        self.file = file

    def write_bad_log(self, line, message):
        with open(self.bad_log, mode='a', encoding='utf8') as log_file:
            message = str(datetime.now()) + ' ' + str(message) + str(line) + '\n'
            log_file.write(message)

    def write_good_log(self, line):
        with open(self.good_log, mode='a', encoding='utf8') as log_file:
            message = str(line) + '\n'
            log_file.write(message)

    def analise_name(self):
        self.name.isalpha()

    def activate_analizer(self):
        with open(self.file, mode='r', encoding='utf8') as read_file:
            for line in read_file:
                self.name, self.email, self.ear = line[:-1].split(sep=' ')
                self.analise_name()
                self.analise_email()
                self.analise_ear()


reg = Analise_reg()
reg.activate_analizer()
