# -*- coding: utf-8 -*-
from random import randint

_num_of_mov = 0
_number = ''
next_number = None


def init_game():
    global _number
    _number = ''
    _number = _number + str(randint(1, 9))
    while len(_number) < 4:
        next_number = str(randint(0, 9))
        _number = _number if _number.find(next_number) >= 0 else _number + next_number
    print(_number)


def check_number(number):
    global _num_of_mov
    bulls, cow, res = 0, 0, False
    if len(set(number)) == 4 and number.isdigit():
        for i in range(4):
            if _number[i] == number[i]:
                bulls += 1
            else:
                cow = cow + 1 if _number.find(number[i]) >= 0 else cow
        _num_of_mov += 1
        res = True
    else:
        res = False

    return bulls, cow, res


def game_over(number):
    if _number == number:
        return True
    else:
        return False


def number_of_moves():
    global _num_of_mov
    return _num_of_mov


def get_number():
    return _number
