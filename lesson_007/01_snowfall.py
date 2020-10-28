# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 500)

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    x = 40
    y = 500
    length = 30

    def __init__(self):
        self.x = Snowflake.x
        self.y = Snowflake.y
        self.length = Snowflake.length
        pass

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, color=sd.background_color, length=self.length)

    def move(self):
        self.y -= random.randint(20,30)
        self.x += random.randint(-20,20)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, color=sd.COLOR_YELLOW, length=self.length)

    def can_fall(self):
        if self.y < 20:
            return False
        else:
            return True



# TODO здесь ваш код

flake = Snowflake()


while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

def get_flakes(count):
    list_flakes =[]
    x_pred = 0
    while len(list_flakes) < count:
        new_flake = Snowflake()
        x = x_pred + random.randint(70, 100)
        new_flake.length = random.randint(10, 40)
        new_flake.x = x
        list_flakes.append(new_flake)
        x_pred = x
    return list_flakes

def get_fallen_flakes(total):

    if not flake.can_fall():
        total += 1

    return total

def append_flakes(count):
    x_pred = 0
    new_flake = Snowflake()
    x = x_pred + random.randint(100, 1100)
    new_flake.length = random.randint(10, 40)
    new_flake.x = x
    flakes.append(new_flake)
    return flakes


flakes = get_flakes(count = 10)  # создать список снежинок

total = 0

while True:
    for flake in flakes:

        flake.clear_previous_picture()
        flake.move()
        flake.draw()

        fallen_flakes = get_fallen_flakes(total=total)  # подчитать сколько снежинок уже упало
    print(fallen_flakes)
    if fallen_flakes:

        total+=1
        append_flakes(count=fallen_flakes)  # добавить еще сверху

    if fallen_flakes == 100:
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()
