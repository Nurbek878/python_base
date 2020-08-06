# -*- coding: utf-8 -*-

import simple_draw as sd

import snowfall

from snowfall import make_snowflake, print_snowflake, move_snowflake, number_snowflake, delete_snowflake


# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)

snowfall.quantity = 10

make_snowflake()

while True:
    print_snowflake(color = sd.background_color)
    move_snowflake()
    print_snowflake(color = sd.COLOR_YELLOW)
    snowbank = number_snowflake()

    for n in range(snowfall.quantity):
        if snowbank[n] == 1:

            delete_snowflake(n=n)

    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
