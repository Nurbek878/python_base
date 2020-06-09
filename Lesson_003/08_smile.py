# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код


def smiley (x, y, new_colour):

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


smiley (300, 300, sd.COLOR_YELLOW)

for _ in range(10):
    x_random = random.randint(0,500)
    y_random = random.randint(0,500)
    smiley(x_random,y_random, sd.COLOR_YELLOW)

sd.pause()