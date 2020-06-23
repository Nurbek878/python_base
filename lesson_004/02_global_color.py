# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код
colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
          sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
try:
    color = int(input('Введите номер цвета фигур:\n 0 - COLOR_RED, \n '
                  '1 - COLOR_ORANGE,\n 2 - COLOR_YELLOW,\n 3 - COLOR_GREEN,\n 4 - COLOR_CYAN,\n 5 - COLOR_BLUE,\n '
                  '6 - COLOR_PURPLE\n'))
except ValueError:
    print('Вы ввели не целое число')
else:
    if 0 <= color <= 6:
        user_color = colors[color]


        def all_func(count_angle, point, angle, angle_rotation, length, width, color):
            for i in range(count_angle + 1):
                angle = angle + angle_rotation
                v = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
                v.draw(color=color)
                point = v.end_point


        # __________ТРЕУГОЛЬНИК_______________

        def triangle(point, angle, length):
            all_func(count_angle=3, point=point, angle=angle, angle_rotation=120, length=length, width=3, color=user_color)


        point_0 = sd.get_point(200, 100)
        triangle(point_0, 0, 100)


        # __________КВАДРАТ_______________
        def square(point, angle, length):
            all_func(count_angle=4, point=point, angle=angle, angle_rotation=90, length=length, width=3, color=user_color)


        point_0 = sd.get_point(400, 100)
        square(point_0, 0, 100)


        # __________ПЯТИУГОЛЬНИК_______________
        def pentagon(point, angle, length):
            all_func(count_angle=5, point=point, angle=angle, angle_rotation=72, length=length, width=3, color=user_color)


        point_0 = sd.get_point(200, 300)
        pentagon(point_0, 0, 100)


        # __________ШЕСТИУГОЛЬНИК_______________
        def hexagon(point, angle, length):
            all_func(count_angle=6, point=point, angle=angle, angle_rotation=60, length=length, width=3, color=user_color)


        point_0 = sd.get_point(400, 300)
        hexagon(point_0, 0, 100)
        sd.pause()
    else:
        print('Вы ввели неверное число')



