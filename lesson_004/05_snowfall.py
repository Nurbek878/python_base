# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
sd.resolution = (1200, 700)
N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
# TODO здесь ваш код

# Формируем списки координат наших снежинок из 20 элементов
x = 0
y = 500

list_x = []
list_y = []
list_length = []

for x in range(100, 1051, 50):
    list_x.append(x)
for y in range(750, 730, -1):
    list_y.append(y)
for i in range(20):
    list_length.append(sd.random_number(10, 50))

end = 0 # Флаг выхода из цикла

# Формируем списки координат наших снежинок из 20 элементов (предыдущие положения). Нач знач задаем как у (x, y)
x_old = []
y_old = []
length_old = []

for x in range(100, 1051, 50):
    x_old.append(x)
for y in range(750, 730, -1):
    y_old.append(y)
for i in range(20):
    length_old.append(sd.random_number(10, 50))

# Формируем список флагов достижения сугроба. Начальные значения задаем 0
snowbank = []
for _ in range(20):
    snowbank.append(0)
# Формируем список из 20 единиц
list_1 = []
for _ in range(20):
    snowbank.append(1)


while True:
    # sd.clear_screen()
    sd.start_drawing()
    for n in range(20):

        # Стираем старую снежинку
        point_old = sd.get_point(x_old[n], y_old[n])
        sd.snowflake(center=point_old, color=sd.background_color, length=list_length[n])

        # Рисуем новую снежинку
        point = sd.get_point(list_x[n], list_y[n])
        sd.snowflake(center=point, color=sd.COLOR_WHITE, length=list_length[n])

        x_old[n] = list_x[n]
        y_old[n] = list_y[n]
        length_old[n] = list_length[n]

        speed_y = sd.random_number(1, 50)
        speed_x = sd.random_number(-20, 20)

        # Определяем достигла ли снежинка сугроба
        if snowbank[n] !=1:
            list_y[n] -= speed_y
            list_x[n] += speed_x

        # Если снежинка достигла земли то выставляем флаг достижения сугроба
        if list_y[n] < 50:
            snowbank[n] = 1
        if snowbank == list_1:
            end = 1
    if end == 1:
        break

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
