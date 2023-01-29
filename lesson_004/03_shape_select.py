# -*- coding: utf-8 -*-
import math

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
# радиус описанной окружности треугольльника = radius = lenght/(3**0.5)
# радиус описанной окружности квадрата = radius = lenght*2*(2**0.5)
# радиус описанной окружности пятиугольника = radius = lenght*0.1*((50+10*(5**0.5)**0.5)
# радиус описанной окружности шестиугольника = radius = lenght


def traingle(figura=3, x=300, y=300, angle=0, lenght=100, color=0):
    figura_angle = {3: 120, 4: 90, 5: 72, 6: 60}
    figura_color_sheet = {0: (255, 0, 0), 1: (255, 127, 0), 2: (255, 255, 0), 3: (0, 255, 0), 4: (0, 255, 255),
                          5: (0, 0, 255), 6: (255, 0, 255)}

    color_figura = figura_color_sheet[color]
    figura_width = 1
    x_coord = 0
    y_coord = 0
    angle_draw = (180 - figura_angle[figura])/2 - angle
    if figura == 3:
        radius = lenght / (3 ** 0.5)
        x_coord = math.cos(math.radians(angle_draw)) * radius
        y_coord = math.sin(math.radians(angle_draw)) * radius
    elif figura == 4:
        radius = (lenght/2)*(2**0.5)
        x_coord = math.cos(math.radians(angle_draw)) * radius
        y_coord = math.sin(math.radians(angle_draw)) * radius
    elif figura == 5:
        radius = lenght*0.1*((50+10*(5**0.5))**0.5)
        x_coord = math.cos(math.radians(angle_draw)) * radius
        y_coord = math.sin(math.radians(angle_draw)) * radius
    elif figura == 6:
        radius = lenght
        x_coord = math.cos(math.radians(angle_draw)) *radius
        y_coord = math.sin(math.radians(angle_draw)) * radius
    else:
        print('некорректный выбор фигуры')
        return
    sd.circle(sd.get_point(x, y), 10, width=3, color=(255, 0, 0))
    sd.circle(sd.get_point(x + x_coord, y - y_coord), 10, width=3, color=(255, 0, 255))
    point = sd.get_point(x + x_coord, y - y_coord)
    vector_start = sd.get_vector(start_point=point, angle=figura_angle[figura] + angle, length=0,
                                 width=figura_width)
    for i in range(1, figura):
        vector = sd.get_vector(start_point=vector_start.end_point, angle=figura_angle[figura] * i + angle,
                               length=lenght, width=figura_width)
        vector.draw(color=color_figura)
        vector_start = vector
    sd.line(start_point=vector.end_point, end_point=point, color=color_figura, width=figura_width)


sd.set_screen_size(1920, 1080)
sd.background_color = (0,0,0)
figura, x, y, angle, lenght, color = 3, 960, 540, 0, 400, 2
print("Пивет! \nНачнем рисовать фигуры")
# figura = input('Введи число углов фигуры =')

# x = input('Введи координату X =')
# y = input('Введи координату Y =')
# angle = input('Введи угол поворота фигуры =')
# lenght = input('Введи длину стороны фигуры =')
figura, x, y, angle, lenght = int(figura), int(x), int(y), int(angle), int(lenght)
# color = input('Выбери цвет фигуры \n0-RED, 1-ORANGE, 2-YELLOW, 3-GREEN, 4-CYAN, 5-BLUE, 6-PURPLE\n')
color = int(color)
# traingle(figura,x,y,angle,lenght)
traingle(4, 150, 700, 135, 200, 3)
traingle(3, 200, 200, 49, 200, 5)
traingle(5, 600, 400, 10, 300, 0)
traingle(6, 1300, 400, 80, 400, 2)


sd.pause()
