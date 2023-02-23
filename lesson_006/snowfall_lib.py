# -*- coding: utf-8 -*-

import simple_draw as sd

x_begin = 0
x_end = sd.resolution[0]
x_snow = []
y_snow = []
lenght_snow = []
max_lenght_snowy = 30


def draw_snow_bcgrnd():
    N = len(x_snow)
    sd.start_drawing()
    for i in range(N):
        point = sd.get_point(x_snow[i], y_snow[i])
        sd.snowflake(center=point, length=lenght_snow[i], color=sd.background_color)
    sd.finish_drawing()
    pass


def create_snow(number_of_snowflakes):
    for i in range(number_of_snowflakes):
        x_snow.append(sd.random_number(0, x_end))
        y_snow.append(sd.random_number(100, sd.resolution[1]))
        lenght_snow.append(sd.random_number(10, max_lenght_snowy))


def draw_snowflakes(color_snowflakes):
    sd.start_drawing()
    N = len(x_snow)
    for i in range(N):
        point = sd.get_point(x_snow[i], y_snow[i])
        sd.snowflake(center=point, length=lenght_snow[i], color=color_snowflakes)
    sd.finish_drawing()


def move_snowflakes():
    N = len(x_snow)
    for i in range(N):
        if x_snow[i] < x_begin:
            x_snow[i] = x_snow[i] + sd.random_number(0, 20)
        elif x_snow[i] > x_end:
            x_snow[i] = x_snow[i] - sd.random_number(0, 20)
        else:
            x_snow[i] = x_snow[i] + sd.random_number(-10, 10)
        y_snow[i] = y_snow[i] - lenght_snow[i] / 2


def fell_snowflakes():
    felling_list_num = []
    N = len(y_snow)
    for i in range(N):
        if y_snow[i] <= lenght_snow[i]:
            felling_list_num.append(i)
    return felling_list_num


def del_snowy(felling_list_number):
    felling_list_number.sort()
    felling_list_number.reverse()
    for i in felling_list_number:
        del (x_snow[i])
        del (y_snow[i])
        del (lenght_snow[i])


def snowy(x_begin=20, x_end=600, hight=600, snowi_cost=10):
    """рисует падающие снежинки
    в параметрах начальная позиция по Х и конечная
    hight - высота задается в параметрах
    и количество снежинок
    """

    # N = snowi_cost  # число снежинок
    # x_snow = []
    # y_snow = []
    # lenght_snow = []
    # max_lenght_snowy = 50
    # for i in range(N):
    #     x_snow.append(sd.random_number(x_begin, x_end))
    #     y_snow.append(sd.random_number(100, hight))
    #     lenght_snow.append(sd.random_number(10, max_lenght_snowy))

    while True:
        # sd.start_drawing()
        # for i in range(N):
        #     point = sd.get_point(x_snow[i], y_snow[i])
        #     sd.snowflake(center=point, length=lenght_snow[i])
        # sd.finish_drawing()
        # sd.sleep(0.05)
        # for i in range(N):
        #     if y_snow[i] > lenght_snow[i]:
        # point = sd.get_point(x_snow[i], y_snow[i])
        # sd.start_drawing()
        # sd.snowflake(center=point, length=lenght_snow[i], color=sd.background_color)
        # sd.finish_drawing()
        # else:
        #     x_snow[i] = sd.random_number(x_begin, x_end)
        #     y_snow[i] = hight + max_lenght_snowy
        #     lenght_snow[i] = sd.random_number(10, max_lenght_snowy)

        # if x_snow[i] < x_begin:
        #     x_snow[i] = x_snow[i] + sd.random_number(0, 20)
        # elif x_snow[i] > x_end:
        #     x_snow[i] = x_snow[i] - sd.random_number(0, 20)
        # else:
        #     x_snow[i] = x_snow[i] + sd.random_number(-10, 10)
        # y_snow[i] = y_snow[i] - lenght_snow[i] / 2
        if sd.user_want_exit():
            break

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
