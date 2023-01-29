# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
from math import ceil


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
def rainbow(x=300, y=300, size=1):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    step = 0
    x,y = x-1700,y-1200
    point = sd.get_point(x, y)
    for color in rainbow_colors:
        sd.start_drawing()
        sd.circle(center_position=point, radius=2000 + step, color=color, width=ceil(size*30))
        sd.finish_drawing()
        step += ceil(30*size)


if __name__ == '__main__':
    sd.set_screen_size(1920,1080)
    rainbow(1800,900,1)
    sd.pause()
