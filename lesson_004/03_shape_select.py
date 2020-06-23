# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код
# -*- coding: utf-8 -*-
import simple_draw as sd

user_color = sd.COLOR_YELLOW
point_0 = sd.get_point(350, 250)

try:
    figure = int(input('Введите номер фигуры:\n '
                       '0 : ТРЕУГОЛЬНИК,\n 1 : КВАДРАТ,\n 2 : ПЯТИУГОЛЬНИК,\n 3 : ШЕСТИУГОЛЬНИК,\n '))
except ValueError:
    print('Вы ввели не целое число')
else:
    if 0 <= figure <= 3:

        def all_func(count_angle, point, angle, angle_rotation, length, width, color):
            for i in range(count_angle + 1):
                angle = angle + angle_rotation
                v = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
                v.draw(color=color)
                point = v.end_point

        if figure == 0:
            # __________ТРЕУГОЛЬНИК_______________

            def triangle(point, angle, length):
                all_func(count_angle=3, point=point, angle=angle, angle_rotation=120, length=length, width=3, color=user_color)


            triangle(point_0, 0, 100)

        elif figure == 1:

            # __________КВАДРАТ_______________
            def square(point, angle, length):
                all_func(count_angle=4, point=point, angle=angle, angle_rotation=90, length=length, width=3, color=user_color)


            square(point_0, 0, 100)

        elif figure == 2:

            # __________ПЯТИУГОЛЬНИК_______________
            def pentagon(point, angle, length):
                all_func(count_angle=5, point=point, angle=angle, angle_rotation=72, length=length, width=3, color=user_color)



            pentagon(point_0, 0, 100)

        elif figure == 3:

            # __________ШЕСТИУГОЛЬНИК_______________
            def hexagon(point, angle, length):
                all_func(count_angle=6, point=point, angle=angle, angle_rotation=60, length=length, width=3, color=user_color)


            hexagon(point_0, 0, 100)

        sd.pause()
    else:
        print('Вы ввели неверное число')



