import simple_draw as sd

# TODO здесь ваш код

import simple_draw as sd


sd.resolution = (1200, 600)


def draw_branches(point, angle, length):

    if length < 5:
        return
    delta = 30
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()
    next_point = v1.end_point
    next_angle_1 = angle - delta
    next_angle_2 = angle + delta
    next_length = length * .75
    draw_branches(point=next_point, angle=next_angle_1, length=next_length)
    draw_branches(point=next_point, angle=next_angle_2, length=next_length)


point_0 = sd.get_point(800, 30)
draw_branches(point=point_0, angle=90, length=100)


sd.pause()







