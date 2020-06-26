

from lesson_005.village.my_rainbow import rainbow


print(dir(rainbow))
rainbow()
# sd.resolution = (1200, 700)


#
# #___________ СМАЙЛИК___________
#
# def smiley (x, y, new_colour):
#
#     point = sd.get_point(x,y)
#     point_left_eye = sd.get_point(x - 15, y + 12)
#     point_right_eye = sd.get_point(x + 15, y + 12)
#     sd.circle (point, radius = 50, color = new_colour, width=1)             #круг
#     sd.circle (point_left_eye, radius = 3, color = new_colour, width=2 )    #левый глаз
#     sd.circle(point_right_eye, radius=3, color=new_colour, width=2)         #правый глаз
#
#     point_mouth_1 = sd.get_point(x - 17, y - 15)
#     point_mouth_2 = sd.get_point(x - 2, y - 20)
#     point_mouth_3 = sd.get_point(x + 2 , y - 20)
#     point_mouth_4 = sd.get_point(x + 17, y - 15)
#     list_point = [point_mouth_1, point_mouth_2, point_mouth_3, point_mouth_4]
#     sd.lines(point_list = list_point, color=sd.COLOR_YELLOW, closed=False, width=1)
#
#
# smiley (700, 100, sd.COLOR_YELLOW)
#
#
# #_____________РАДУГА______________
#
# def rainbow():
#     radius = 750
#     rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
#                        sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
#     for color in rainbow_colors:
#
#         #радуга дугами от окружности
#
#         point_circle = sd.get_point(400, 0)
#         radius += 10
#         sd.circle(center_position=point_circle, radius=radius, color=color, width=10)
# rainbow()
#
# #__________ДЕРЕВО_______________
#
# def draw_branches(point, angle, length):
#
#     if length < 5:
#         return
#     delta = 30
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle_1 = angle - delta
#     next_angle_2 = angle + delta
#     next_length = length * .75
#     draw_branches(point=next_point, angle=next_angle_1, length=next_length)
#     draw_branches(point=next_point, angle=next_angle_2, length=next_length)
#
#
# point_0 = sd.get_point(800, 30)
# draw_branches(point=point_0, angle=90, length=100)
#
#
# #_________СТЕНА_____________
#
# def bricks (x_begin, y_begin):
#     for x in range(x_begin, 401, 50):
#         for y in range (y_begin, 301, 50):
#             point_1 = sd.get_point(x, y)
#             point_2 = sd.get_point(x + 50, y + 25)
#             sd.rectangle(left_bottom = point_1, right_top = point_2, color=sd.COLOR_RED, width=1)
#
# point_left = sd.get_point(150,0)
# sd.vector(point_left, 90, 300, sd.COLOR_RED, 1)
# point_right = sd.get_point(450,0)
# sd.vector(point_right, 90, 300, sd.COLOR_RED, 1)
# bricks(150,0)
# bricks(175,25)
#
#
# #___________КРЫША ДОМА_________
#
# def triangle(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 150, length=length-127, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 210, length=length-127, width=3)
#     v3.draw()
#
#
# point_0 = sd.get_point(150, 325)
# triangle(point=point_0, angle=0, length=300)
#
# #_______________СНЕЖИНКИ____________
# # -*- coding: utf-8 -*-
#
# import simple_draw as sd
#
# N = 20
#
# x = 0
# y = 500
#
# list_x = []
# list_y = []
# list_length = []
#
# for x in range(100, 1051, 50):
#     list_x.append(x)
# for y in range(750, 730, -1):
#     list_y.append(y)
# for i in range(20):
#     list_length.append(sd.random_number(10, 50))
#
# end = 0 # Флаг выхода из цикла
#
# # Формируем списки координат наших снежинок из 20 элементов (предыдущие положения). Нач знач задаем как у (x, y)
# x_old = []
# y_old = []
# length_old = []
#
# for x in range(100, 1051, 50):
#     x_old.append(x)
# for y in range(750, 730, -1):
#     y_old.append(y)
# for i in range(20):
#     length_old.append(sd.random_number(10, 50))
#
# # Формируем список флагов достижения сугроба. Начальные значения задаем 0
# snowbank = []
# for _ in range(20):
#     snowbank.append(0)
# # Формируем список из 20 единиц
# list_1 = []
# for _ in range(20):
#     snowbank.append(1)
#
#
# while True:
#     # sd.clear_screen()
#     sd.start_drawing()
#     for n in range(20):
#
#         # Стираем старую снежинку
#         point_old = sd.get_point(x_old[n], y_old[n])
#         sd.snowflake(center=point_old, color=sd.background_color, length=list_length[n])
#
#         # Рисуем новую снежинку
#         point = sd.get_point(list_x[n], list_y[n])
#         sd.snowflake(center=point, color=sd.COLOR_WHITE, length=list_length[n])
#
#         x_old[n] = list_x[n]
#         y_old[n] = list_y[n]
#         length_old[n] = list_length[n]
#
#         speed_y = sd.random_number(1, 50)
#         speed_x = sd.random_number(-20, 20)
#
#         # Определяем достигла ли снежинка сугроба
#         if snowbank[n] !=1:
#             list_y[n] -= speed_y
#             list_x[n] += speed_x
#
#         # Если снежинка достигла земли то выставляем флаг достижения сугроба
#         if list_y[n] < 50:
#             snowbank[n] = 1
#         if snowbank == list_1:
#             end = 1
#     if end == 1:
#         break
#
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break



sd.pause()