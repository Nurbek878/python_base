# -*- coding: utf-8 -*-

# (цикл for)


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

import simple_draw as sd
sd.resolution = (1200, 600)


def bricks (x_begin, y_begin):
    for x in range(x_begin, 401, 50):
        for y in range (y_begin, 301, 50):
            point_1 = sd.get_point(x, y)
            point_2 = sd.get_point(x + 50, y + 25)
            sd.rectangle(left_bottom = point_1, right_top = point_2, color=sd.COLOR_RED, width=1)

point_left = sd.get_point(150,0)
sd.vector(point_left, 90, 300, sd.COLOR_RED, 1)
point_right = sd.get_point(450,0)
sd.vector(point_right, 90, 300, sd.COLOR_RED, 1)
bricks(150,0)
bricks(175,25)




sd.pause()