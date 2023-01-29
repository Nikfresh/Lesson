# -*- coding: utf-8 -*-

import simple_draw as sd


def snowy(x_begin=20, x_end=600,y_min=0, y_max=600, snowi_cost=10):
    """рисует падающие снежинки
    в параметрах начальная позиция по Х и конечная
    hight - высота задается в параметрах
    и количество снежинок
    """

    N = snowi_cost  # число снежинок
    x_snow = []
    y_snow = []
    lenght_snow = []
    max_lenght_snowy = 20
    for i in range(N):
        x_snow.append(sd.random_number(x_begin, x_end))
        y_snow.append(sd.random_number(y_min, y_max))
        lenght_snow.append(sd.random_number(10, max_lenght_snowy))

    while True:
        sd.start_drawing()
        for i in range(N):
            point = sd.get_point(x_snow[i], y_snow[i])
            sd.snowflake(center=point, length=lenght_snow[i])
        sd.finish_drawing()
        sd.sleep(0.01)
        for i in range(N):
            if y_snow[i] > lenght_snow[i]+y_min:
                point = sd.get_point(x_snow[i], y_snow[i])
                sd.start_drawing()
                sd.snowflake(center=point, length=lenght_snow[i], color=sd.background_color)
                sd.finish_drawing()
            else:
                x_snow[i] = sd.random_number(x_begin, x_end)
                y_snow[i] = y_max + max_lenght_snowy
                lenght_snow[i] = sd.random_number(10, max_lenght_snowy)

            if x_snow[i] < x_begin:
                x_snow[i] = x_snow[i] + sd.random_number(0, 20)
            elif x_snow[i] > x_end:
                x_snow[i] = x_snow[i] - sd.random_number(0, 20)
            else:
                x_snow[i] = x_snow[i] + sd.random_number(-10, 10)
            y_snow[i] = y_snow[i] - lenght_snow[i] / 2
        if sd.user_want_exit():
            break
if __name__ == '__main__':
    snowy()
    sd.pause()

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
