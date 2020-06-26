# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd



def smiley (x, y, new_colour):
    import simple_draw as sd
    point = sd.get_point(x,y)
    point_left_eye = sd.get_point(x - 15, y + 12)
    point_right_eye = sd.get_point(x + 15, y + 12)
    sd.circle (point, radius = 50, color = new_colour, width=1)             #круг
    sd.circle (point_left_eye, radius = 3, color = new_colour, width=2 )    #левый глаз
    sd.circle(point_right_eye, radius=3, color=new_colour, width=2)         #правый глаз

    point_mouth_1 = sd.get_point(x - 17, y - 15)
    point_mouth_2 = sd.get_point(x - 2, y - 20)
    point_mouth_3 = sd.get_point(x + 2 , y - 20)
    point_mouth_4 = sd.get_point(x + 17, y - 15)
    list_point = [point_mouth_1, point_mouth_2, point_mouth_3, point_mouth_4]
    sd.lines(point_list = list_point, color=sd.COLOR_YELLOW, closed=False, width=1)


smiley (700, 100, sd.COLOR_YELLOW)

def my_func_1():
    print('Я тестовая функция')
sd.pause()