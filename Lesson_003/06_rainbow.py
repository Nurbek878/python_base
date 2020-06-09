# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                   sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
sd.resolution = (600, 600)

x = 0
y = 0
radius = 500

for color in rainbow_colors:

    # 7 линий разного цвета

    point_1 = sd.get_point(50 + x,50)
    point_2 = sd.get_point(350 + x,450)
    x += 5
    sd.line(point_1, point_2, color = color, width=2)

    #радуга дугами от окружности

    point_circle = sd.get_point(300, 0)
    radius += 10
    sd.circle(center_position=point_circle, radius=radius, color=color, width=10)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код


sd.pause()
