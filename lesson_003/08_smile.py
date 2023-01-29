# -*- coding: utf-8 -*-
# (определение функций)
import simple_draw as sd
from math import ceil


def linerer(x, y, point_l, color, width):
    i = 0
    while i < (len(point_l) - 1):
        sd.start_drawing()
        sd.line(start_point=sd.get_point(x + point_l[i][0], y + point_l[i][1]),
                end_point=sd.get_point(x + point_l[i + 1][0], y + point_l[i + 1][1]), color=color, width=width)
        i += 1
        sd.finish_drawing()


def print_smile(x=100, y=100, size=1):
    center_smile_point = sd.get_point(x, y)
    sd.start_drawing()
    sd.circle(center_smile_point, ceil(50 * size), sd.COLOR_YELLOW, ceil(4 * size))
    sd.circle(sd.get_point(x - ceil(20 * size), y + ceil(10 * size)), ceil(10 * size), sd.COLOR_YELLOW, ceil(2 * size))
    sd.circle(sd.get_point(x + ceil(20 * size), y + ceil(10 * size)), ceil(10 * size), sd.COLOR_YELLOW, ceil(2 * size))
    sd.circle(sd.get_point(x - ceil(18 * size), y + ceil(10 * size)), ceil(1 * size), sd.COLOR_YELLOW, ceil(2 * size))
    sd.circle(sd.get_point(x + ceil(22 * size), y + ceil(10 * size)), ceil(1 * size), sd.COLOR_YELLOW, ceil(2 * size))
    sd.finish_drawing()
    point_l = [-ceil(30 * size), -ceil(15 * size)], [-ceil(10 * size), -ceil(25 * size)], [ceil(10 * size),
                                                                                           -ceil(25 * size)], [
        ceil(30 * size), -ceil(15 * size)]
    linerer(x, y, point_l, sd.COLOR_YELLOW, ceil(2 * size))
    point_l = [ceil(0 * size), ceil(5 * size)], [-ceil(5 * size), -ceil(10 * size)], [ceil(5 * size), -ceil(10 * size)]
    linerer(x, y, point_l, sd.COLOR_YELLOW, ceil(2 * size))


def human_drawing(x=100, y=200, size=1):
    point_l = [-ceil(50 * size), -ceil(100 * size)], [0, - ceil(50 * size)], [ceil(50*size), - ceil(100 * size)]
    linerer(x, y, point_l, sd.COLOR_YELLOW, ceil(8 * size))
    point_l = [0, - ceil(50 * size)], [0, - ceil(150 * size)]
    print_smile(x, y, size)
    linerer(x, y, point_l, sd.COLOR_YELLOW, ceil(8 * size))
    point_l = [-ceil(50 * size), -ceil(250 * size)], [0, - ceil(150 * size)], [ceil(50 * size), - ceil(250 * size)]
    linerer(x, y, point_l, sd.COLOR_YELLOW, ceil(8 * size))


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
if __name__ == '__main__':
    # for i in range(10):
    #     x_rand = sd.randint(50, 550)
    #     y_rand = sd.randint(50, 550)
    #     print_smile(x_rand, y_rand, i * 0.2)
    human_drawing(300, 500, 1)
    sd.pause()
