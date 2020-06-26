# -*- coding: utf-8 -*-

import simple_draw as sd


def rainbow():
    import simple_draw as sd
    radius = 750
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                       sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    for color in rainbow_colors:

        #радуга дугами от окружности

        point_circle = sd.get_point(400, 0)
        radius += 10
        sd.circle(center_position=point_circle, radius=radius, color=color, width=10)



sd.pause()

