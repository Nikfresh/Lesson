# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x_snow = (sd.random_number(0, sd.resolution[0]))
        self.y_snow = (sd.random_number(sd.resolution[1] - 40, sd.resolution[1]))
        self.lenght_snow = (sd.random_number(10, 30))

    def move(self):
        if self.x_snow < 10:
            self.x_snow += sd.random_number(0, 20)
        elif self.x_snow > sd.resolution[0] - 10:
            self.x_snow -= sd.random_number(0, 20)
        else:
            self.x_snow += sd.random_number(-10, 10)
        self.y_snow -= self.lenght_snow / 2

    def draw(self):
        point = sd.get_point(self.x_snow, self.y_snow)
        sd.start_drawing()
        sd.snowflake(center=point, length=self.lenght_snow, color=sd.COLOR_WHITE)
        sd.finish_drawing()

    def clear_previous_picture(self):
        point = sd.get_point(self.x_snow, self.y_snow)
        sd.start_drawing()
        sd.snowflake(center=point, length=self.lenght_snow, color=sd.background_color)
        sd.finish_drawing()

    def can_fall(self):
        if self.y_snow >= self.lenght_snow:
            return True
        if self.y_snow < self.lenght_snow:
            return False


def append_flakes(count=0):
    for i in range(0, count):
        flakes.append(Snowflake())


def get_flakes(count=10):
    flakes_list = []
    for i in range(0, count):
        flakee = Snowflake()
        flakes_list.append(flakee)
    return flakes_list


def get_fallen_flakes():
    list_fallen_flakes = []
    for i, flaker in enumerate(flakes):
        if flaker.can_fall() == False:
            list_fallen_flakes.append(i)
    count_fall_flakes = len(list_fallen_flakes)
    list_fallen_flakes.sort()
    list_fallen_flakes.reverse()
    for i in list_fallen_flakes:
        del flakes[i]
    return count_fall_flakes


flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=50)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
