# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def color(n):
    r = 510 / (2 * n)
    # r=randint(20,255)
    # g=randint(20,255)
    # b=randint(20,255)
    return (255, r, r)


def get_polygon(n):
    if n < 3:
        raise ValueError('Количесство углов менее 3')
    figura_angle = 180 - ((n - 2) * 180 / n)

    def polygon(x=300, y=300, angle=3, lenght=100):
        point = sd.get_point(x, y)
        figura_width = 1
        vector_start = sd.get_vector(start_point=point, angle=figura_angle + angle, length=0,
                                     width=figura_width)
        for i in range(1, n + 1):
            vector = sd.get_vector(start_point=vector_start.end_point, angle=figura_angle * i + angle,
                                   length=lenght, width=figura_width)
            color_figura = tuple(color(i))
            vector.draw(color=(color_figura))
            vector_start = vector
        # sd.line(start_point=vector.end_point, end_point=point, color=color_figura, width=figura_width)

    return polygon


sd.set_screen_size(1920, 1080)
draw_triangle = []
draw_triangle = [get_polygon(n) for n in range(3, 15)]
# args = [x:200,y:300, angle:0, lenght: 100]
args = [1000, 100, 0, 250]
for num in range(len(draw_triangle)):
    draving = draw_triangle[num]
    draving(*args)

# figura_angle = [180 - ((n - 2) * 180 / n) for n in range(3, 20)]
# print(type(figura_angle))
# print(figura_angle)
sd.pause()
