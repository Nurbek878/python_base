# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

import simple_draw as sd

task = 3
sd.resolution = (800, 600)

point_0 = sd.get_point(300, 30)

# 1) Первое задание.
if task == 1:
    def draw_branches(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle - 30, length=length, width = 3)
        v1.draw()
        v2 = sd.get_vector(start_point=point, angle=angle + 30, length=length, width = 3)
        v2.draw()


    draw_branches(point = point_0, angle = 45, length = 200)


# 2) Второе задание
if task == 2:
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


    draw_branches(point=point_0, angle=90, length=100)

    sd.pause()

# 4) Усложненное задание

if task == 3:
    def draw_branches(point, angle, length):
        if length < 3:
            return
        delta = sd.random_number(30-0.4*30, 30+0.4*30)
        next_length = sd.random_number(int(length * (0.75 - 0.2 * 0.75)), int(length * (0.75 + 0.2 * 0.75)))

        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        v1.draw()
        next_point = v1.end_point
        next_angle_1 = angle - delta
        next_angle_2 = angle + delta

        draw_branches(point=next_point, angle=next_angle_1, length=next_length)
        draw_branches(point=next_point, angle=next_angle_2, length=next_length)


    draw_branches(point=point_0, angle=90, length=100)

    sd.pause()

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()


