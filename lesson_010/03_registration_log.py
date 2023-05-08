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
class NotNameError(Exception):
    pass
class NotEmailError(Exception):
    pass

class Analise_reg():

    def __init__(self, file='registrations.txt'):
        self.good_log = 'registrations_good.log'
        self.bad_log = 'registrations_bad.log'
        self.file = file
        with open(self.good_log, mode='w', encoding='utf8') as log_file:
            pass
        with open(self.bad_log, mode='w', encoding='utf8') as log_file:
            pass

    def write_bad_log(self, line, message):
        with open(self.bad_log, mode='a', encoding='utf8') as log_file:
            message = str(datetime.now()) + ' ' + str(message) + str(line)
            log_file.write(message)

    def write_good_log(self, line):
        with open(self.good_log, mode='a', encoding='utf8') as log_file:
            message = str(line)
            log_file.write(message)

    def analise_name(self):
        if not self.name.isalpha():
            raise NotNameError ('Поле имени содержит НЕ только буквы')
    def analise_email(self):
        if '@'in self.email and '.' in self.email:
            return
        else:
            raise NotEmailError('Поле емейл НЕ содержит @ и .(точку)')


    def analise_ear(self):
        ear = int(self.ear)
        if self.ear.isdigit() and 10<= ear <= 99 :
            return
        else :
            raise ValueError ('поле_возраст_НЕ_является_числом_от_10_до_99 ')
    def spliter(self,line):
        try:
            self.name, self.email, self.ear = line[:-1].split(sep=' ')
        except ValueError as exc:
            raise ValueError('НЕ присутсвуют все три поля')


    def activate_analizer(self):
        with open(self.file, mode='r', encoding='utf8') as read_file:
            for line in read_file:
                try:
                    self.spliter (line)
                    self.analise_name()
                    self.analise_email()
                    self.analise_ear()
                except ValueError as exc:
                    self.write_bad_log(line=line,message=exc)
                    continue
                except NotNameError as exc:
                    self.write_bad_log(line=line,message=exc)
                    continue
                except NotEmailError as exc:
                    self.write_bad_log(line=line,message=exc)
                    continue
                self.write_good_log(line=line)



reg = Analise_reg()
reg.activate_analizer()
