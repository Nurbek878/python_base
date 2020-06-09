# -*- coding: utf-8 -*-

# (цикл for)


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

import simple_draw as sd
sd.resolution = (1200, 600)


def bricks (x_begin, y_begin):
    for x in range(x_begin, 1201, 100):
        for y in range (y_begin, 1001, 100):
            point_1 = sd.get_point(x, y)
            point_2 = sd.get_point(x + 100, y + 50)
            sd.rectangle(left_bottom = point_1, right_top = point_2, color=sd.COLOR_YELLOW, width=1)


bricks(0,0)
bricks(50,50)




sd.pause()
