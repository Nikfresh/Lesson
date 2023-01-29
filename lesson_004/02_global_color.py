# -*- coding: utf-8 -*-
import simple_draw as sd


def traingle(figura=3, x=300, y=300, angle=0, lenght=100, color=0):
    figura_angle = {3: 120, 4: 90, 5: 72, 6: 60}
    figura_color_sheet = {0: (255, 0, 0), 1: (255, 127, 0), 2: (255, 255, 0), 3: (0, 255, 0), 4: (0, 255, 255),
                    5: (0, 0, 255), 6: (255, 0, 255)}
    point = sd.get_point(x, y)
    color_figura = figura_color_sheet[color]
    figura_width = 1
    if 3 <= figura <= 6:
        vector_start = sd.get_vector(start_point=point, angle=figura_angle[figura] + angle, length=0,
                                     width=figura_width)
        for i in range(1, figura):
            vector = sd.get_vector(start_point=vector_start.end_point, angle=figura_angle[figura] * i + angle,
                                   length=lenght, width=figura_width)
            vector.draw(color=color_figura)
            vector_start = vector
        sd.line(start_point=vector.end_point, end_point=point, color=color_figura, width=figura_width)
    else:
        print('некорректный выбор фигуры')


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

sd.set_screen_size(1920, 1080)
color = 0
print("Пивет! \nНачнем рисовать фигуры")
# figura = input('Введи число углов фигуры =')
# x = input('Введи координату X =')
# y = input('Введи координату Y =')
# angle = input('Введи угол поворота фигуры =')
# lenght = input('Введи длину стороны фигуры =')
# figura,x,y,angle,lenght = int(figura),int(x),int(y),int(angle),int(lenght)
color = input('Выбери цвет фигуры \n0-RED, 1-ORANGE, 2-YELLOW, 3-GREEN, 4-CYAN, 5-BLUE, 6-PURPLE\n')
color = int(color)
# traingle(figura,x,y,angle,lenght)
traingle(3, 200, 300, 25, 50, color)
traingle(4, 500, 300, 10, 100, color)
traingle(5, 600, 800, 5, 150, color)
traingle(6, 1500, 200, 0, 300, color)

sd.pause()
