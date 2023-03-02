# -*- coding: utf-8 -*-
from random import randint

from termcolor import cprint, colored


# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
class Lava:
    def __init__(self):
        pass

    def __str__(self):
        return colored("Лава",color= 'red',on_color= 'on_green')


class Dust:
    def __init__(self):
        pass

    def __str__(self):
        return colored("Пыль",color= 'green',on_color= 'on_white')


class Flash:
    def __init__(self):
        pass

    def __str__(self):
        return "Молния"


class Dirt:
    def __init__(self):
        pass

    def __str__(self):
        return "Грязь"


class Steam:
    def __init__(self):
        pass

    def __str__(self):
        return "Пар"


class Storm:
    def __init__(self):
        pass

    def __str__(self):
        return "Шторм"


class Air:
    def __init__(self):
        pass

    def __str__(self):
        return "Воздух"

    def __add__(self, other):
        if type(other) == type(Fire()):
            new_obj = Flash()
        elif type(other) == type(Earth()):
            new_obj = Dust()
        elif type(other) == type(Water()):
            new_obj = Storm()
        elif type(other) == type(Air()):
            new_obj = Air()
        else:
            new_obj = Air()
        return new_obj


class Water:
    def __init__(self):
        pass

    def __str__(self):
        return "Вода"

    def __add__(self, other):
        if type(other) == type(Fire()):
            new_obj = Steam()
        elif type(other) == type(Earth()):
            new_obj = Dirt()
        elif type(other) == type(Water()):
            new_obj = Water()
        elif type(other) == type(Air()):
            new_obj = Storm()
        else:
            new_obj = Water()
        return new_obj


class Fire:
    def __init__(self):
        pass

    def __str__(self):
        return "Огонь"

    def __add__(self, other):
        if type(other) == type(Fire()):
            new_obj = Fire()
        elif type(other) == type(Earth()):
            new_obj = Lava()
        elif type(other) == type(Water()):
            new_obj = Steam()
        elif type(other) == type(Air()):
            new_obj = Flash()
        else:
            new_obj = Fire()
        return new_obj


class Earth:
    def __init__(self):
        pass

    def __str__(self):
        return "Земля"

    def __add__(self, other):
        if type(other) == type(Fire()):
            new_obj = Lava()
        elif type(other) == type(Earth()):
            new_obj = Earth()
        elif type(other) == type(Water()):
            new_obj = Dirt()
        elif type(other) == type(Air()):
            new_obj = Dust()
        else:
            new_obj = Earth()
        return new_obj


zeml = Earth()
water = Water()
air = Air()
firre = Fire()
pogoda = [Earth(), Water(), Air(), Fire()]
# print(zeml)
# print(zeml + water)
# print(Earth(), '+', Air(), '=', Earth() + Air())
# print(Air(), '+', Earth(), '=', Air() + Earth())
# print(Air(), '+', Fire(), '=', Air() + Fire())
# print(Water(), '+', Air(), '=', Water() + Air())
# print(Air(), '+', Water(), '=', Air() + Water())

i = 0
while i < 20:
    rand = randint(0, 3)
    rand2 = randint(0, 3)
    color = ['green', 'blue', 'cyan', 'red']
    print(colored(pogoda[rand], color[rand]) , '+', colored(pogoda[rand2], color[rand2]) , '=', pogoda[rand] + pogoda[rand2])
    i += 1

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
