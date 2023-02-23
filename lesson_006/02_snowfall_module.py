# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall_lib import *

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
sd.set_screen_size(500, 300)
create_snow(20)
color_snowy = 10
while True:
    color_snowy = color_snowy + 5 if color_snowy <= 249 else 10
    draw_snow_bcgrnd()
    move_snowflakes()
    draw_snowflakes(color_snowflakes=(color_snowy,128,255))
    list_fell = fell_snowflakes()
    if list_fell:
        del_snowy(list_fell)
        create_snow(len(list_fell))
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
