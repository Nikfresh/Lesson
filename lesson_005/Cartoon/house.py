# -*- coding: utf-8 -*-

from math import ceil

import simple_draw as sd


def home(x_begin=0, x_over=500, y_begin=0, y_over=500, rock_lenght=40):
    """
            Рисуем стену из кирпича по координатам левого нижнего и верхнего правого угла
    """
    x_begin, y_begin, x_over, y_over, rock_lenght = ceil(x_begin), ceil(y_begin), ceil(x_over), ceil(y_over), ceil(
        rock_lenght)
    col_wal = sd.COLOR_YELLOW
    step_y = step_y_const = ceil(rock_lenght / 2.5)
    hight = ceil(step_y / 20)
    y_last = ((y_over - y_begin) // step_y) * step_y
    x_stat = False
    win_coord_x, win_coord_y, wall_coord_y, wall_coord_x = [], [], [], []
    y_over = ((y_over - y_begin) // step_y) * step_y
    x_win_begin, x_win_over = (x_over - x_begin) / 3 + x_begin, (x_over - x_begin) * 2 / 3 + x_begin
    y_win_begin, y_win_over = (y_over - y_begin) / 3 + y_begin, (y_over - y_begin) * 4 / 5 + y_begin
    sd.start_drawing()
    sd.line(sd.get_point(x_begin, y_begin), sd.get_point(x_begin, y_over), col_wal, hight)
    sd.line(sd.get_point(x_begin, y_over), sd.get_point(x_over, y_over), col_wal, hight)
    sd.line(sd.get_point(x_over, y_begin), sd.get_point(x_over, y_over), col_wal, hight)
    roof_points = [sd.get_point(x_begin, y_over),
                   sd.get_point(x_begin + (x_over - x_begin) / 2, y_over + (x_over - x_begin) / 3),
                   sd.get_point(x_over, y_over)]
    sd.polygon(roof_points, sd.COLOR_PURPLE, width=0)
    sd.finish_drawing()
    for y in range(y_begin, y_over, step_y):
        wall_coord_y.append(y)
        point_y = sd.get_point(x_begin, y)
        point_end_y = sd.get_point(x_over, y)
        if y > y_last - step_y:
            step_y = y_over - wall_coord_y[-1]
        for x in range(x_begin + int(not (x_stat)) * rock_lenght, x_over - int((rock_lenght * int(x_stat)) / 2),
                       rock_lenght):
            wall_coord_x.append(x)
            point = sd.get_point(x + rock_lenght * int(x_stat) / 2, y)
            point_end = sd.get_point(x + rock_lenght * int(x_stat) / 2, y + step_y - 1)
            if x_win_begin < x < x_win_over and y_win_begin < y < y_win_over:
                win_coord_x.append(x)
                win_coord_y.append(y)
            else:
                sd.start_drawing()
                sd.line(point, point_end, col_wal, hight)
                sd.finish_drawing()
        if y_win_begin < y < y_win_over:
            point_end_y = sd.get_point(win_coord_x[0] - rock_lenght / 2, y)
            sd.start_drawing()
            sd.line(sd.get_point(win_coord_x[-1] + rock_lenght, y), sd.get_point(x_over, y), col_wal, hight)
            sd.finish_drawing()
        sd.start_drawing()
        sd.line(point_y, point_end_y, col_wal, hight)
        sd.sleep(0.05)
        sd.finish_drawing()
        x_stat = not (x_stat)
    x1, y1 = win_coord_x[0] - rock_lenght / 2, win_coord_y[0]
    x2, y2 = win_coord_x[-1] + rock_lenght, win_coord_y[-1] + step_y_const
    x3, y3 = (x2 + x1) / 2, (y2 - y1) / 3 * 2 + y1
    sd.start_drawing()
    sd.line(sd.get_point(x1, y1), sd.get_point(x2, y1), col_wal, hight * 3)  # окно
    sd.line(sd.get_point(x1, y2), sd.get_point(x2, y2), col_wal, hight * 3)  # окно
    sd.line(sd.get_point(x1, y1), sd.get_point(x1, y2), col_wal, hight * 3)  # окно
    sd.line(sd.get_point(x2, y1), sd.get_point(x2, y2), col_wal, hight * 3)  # окно
    sd.line(sd.get_point(x1, y3), sd.get_point(x2, y3), col_wal, hight * 3)  # окно
    sd.line(sd.get_point(x3, y1), sd.get_point(x3, y3), col_wal, hight * 3)  # окно
    sd.finish_drawing()


if __name__ == "__main__":
    sd.set_screen_size(1920, 1080)
    home(100, 400, 100, 600, 40)
    sd.pause()
