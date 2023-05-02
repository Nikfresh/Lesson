# -*- coding: utf-8 -*-
from datetime import datetime
from random import randint


# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def exepting():
    exept = randint(1, 6)
    if exept == 1:
        raise IamGodError('Возомнил себя богом и испарился')
    elif exept == 2:
        raise DrunkError('Напился и сдох')
    elif exept == 3:
        raise CarCrashError('Разбился на тачке и сдох')
    elif exept == 4:
        raise GluttonyError('Обожрался и сдох')
    elif exept == 5:
        raise DepressionError('Cдох от депресии')
    elif exept == 6:
        raise SuicideError('Самоубился')
    else:
        raise Exception('Что-то не так в параметрах функции оня не должна никак попасть сюда!!!')


def write_log(message):
    with open(log, mode='a', encoding='utf8') as log_file:
        message = str(datetime.now()) + ' ' + str(message) + '\n'
        log_file.write(message)


def one_day():
    global Carma
    act_day = randint(1, 13)
    if act_day == 13:
        try:
            exepting()
        except Exception as exc:
            print(f'CRACH DEAD - причина {exc}')
            write_log(exc)
    else:
        carma_day = randint(1, 7)
        # print(f'Сегодня карма повысилась на - {carma_day} пунктов')
        Carma += carma_day


log = 'log_one_day.txt'
ENLIGHTENMENT_CARMA_LEVEL = 7777
Carma = 0
while Carma < ENLIGHTENMENT_CARMA_LEVEL:
    one_day()
# https://goo.gl/JnsDq
