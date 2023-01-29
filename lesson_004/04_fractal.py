# -*- coding: utf-8 -*-
from random import random

from math import ceil

import simple_draw as sd


def draw_branches(point, ang=90, len=100, delta=10, size=1):
    color_tree = (165, 42, 42)
    len = ceil(size * len)
    if len < ceil(8 * size):
        return
    if len < ceil(40 * size):
        color_tree = (0, 255, 0)
    v1 = sd.get_vector(start_point=point, angle=ang + delta, length=len, width=ceil(size * len / 15))
    sd.start_drawing()
    v1.draw(color=color_tree)
    p1, ang2, len2 = v1.end_point, ang + delta, len * (.3 + .6 * random() if len > 30 else .7 + .2 * random())
    v2 = sd.get_vector(start_point=point, angle=ang - delta, length=len, width=ceil(size * len / 15))
    v2.draw(color=color_tree)
    sd.finish_drawing()
    p2, ang3, len3 = v2.end_point, ang - delta, len * (.3 + .6 * random() if len > 30 else .7 + .2 * random())
    draw_branches(point=p1, ang=ang2, len=len2, delta=delta)
    draw_branches(point=p2, ang=ang3, len=len3, delta=-1 * delta)


def tree_draw(x=500, y=100, size=1):
    start_point = sd.get_point(x, y)
    v1 = sd.get_vector(start_point=start_point, angle=ceil(80 + (20 * random())), length=ceil(150*size),
                       width=ceil(size * 150 / 15))
    sd.start_drawing()
    v1.draw(color=(165, 42, 42))
    sd.finish_drawing()
    draw_branches(point=v1.end_point, ang=ceil(80 + (20 * random())), len=ceil(120 * size), delta=25, size=size)


if __name__ == '__main__':
    sd.set_screen_size(1920, 1080)
    # point = sd.get_point(500, 100)
    # draw_branches(point=point, len=150, delta=30)
    tree_draw(1000, 100, 1.21)
    # for _ in range(10):
    #     print(ceil(80 + (20 * random())),' ',end='')

    # 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
    # Функция должна принимать параметры:
    # - точка начала рисования,
    # - угол рисования,
    # - длина ветвей,
    # Отклонение ветвей от угла рисования принять 30 градусов,

    # 2) Сделать draw_branches рекурсивной
    # - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
    # - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
    #   с параметром "угол рисования" равным углу только что нарисованной ветви,
    #   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

    # 3) первоначальный вызов:
    # root_point = get_point(300, 30)
    # draw_bunches(start_point=root_point, angle=90, length=100)

    # Пригодятся функции
    # sd.get_point()
    # sd.get_vector()
    # Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

    # можно поиграть -шрифтами- цветами и углами отклонения



    # 4) Усложненное задание (делать по желанию)
    # - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
    # - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
    # Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

    # Пригодятся функции
    # sd.random_number()

    sd.pause()
