# -*- coding: utf-8 -*-

import simple_draw as sd
from math import ceil

def sunny(x=300, y=300, size=1):
    point = sd.get_point(x, y)
    sd.circle(point,ceil(50*size),color=sd.COLOR_YELLOW,width=0)
    for x in range(15, 376, 45):
        v1=sd.get_vector(start_point=point,angle=x,length=ceil(120*size),width=ceil(8*size))
        v1.draw()


if __name__ == '__main__':
    sd.set_screen_size(1920, 1080)
    sunny(1000, 900, 1)
    sd.pause()
