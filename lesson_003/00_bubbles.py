# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(1000, 100)
radius = 50
for _ in range(3):
    radius += 50
    sd.circle(center_position=point, radius=radius, color=(255, 0, 0), width=1)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг


def buble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=(255, 0, 255), width=1)


point = sd.get_point(300, 500)
buble(point=point, step=10)
# Нарисовать 10 пузырьков в ряд

for x in range(100, 700, 100):
    point = sd.get_point(x, 200)
    sd.circle(center_position=point, radius=20)

# Нарисовать три ряда по 10 пузырьков
for x in range(100, 1100, 100):
    for y in range(300, 600, 100):
        point = sd.get_point(x, y)
        # sd.circle(center_position=point,radius=40,color=(255,255,0),width=3)
        buble(point, 5)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    radius = random.randint(2, 50)
    sd.circle(center_position=point, radius=radius, color=color, width=5)

sd.pause()
