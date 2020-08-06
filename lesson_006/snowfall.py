import simple_draw as sd

sd.resolution = (1200, 500)

quantity = 20


def make_snowflake():
    global list_x, list_y, list_length, point
    x = 40
    y = 800

    list_x = []
    list_y = []
    list_length = []
    point = []

    for n in range(quantity):
        list_x.append(x)
        list_y.append(y)
        list_length.append(sd.random_number(10, 40))
        point.append(sd.get_point(list_x[n], list_y[n]))
        sd.snowflake(center=point[n], color=sd.COLOR_YELLOW, length=list_length[n])

        x += 70
        y -= 1


def print_snowflake(color):
    for n in range(quantity):
        point[n] = sd.get_point(list_x[n], list_y[n])
        sd.snowflake(center=point[n], color=color, length=list_length[n])


def move_snowflake():
    for n in range(quantity):
        move = sd.random_number(10, 50)
        list_y[n] -= move


def number_snowflake():
    snowbank = []
    for _ in range(quantity):
        snowbank.append(0)

    for n in range(quantity):
        if list_y[n] < 0:
            snowbank[n] = 1
    return snowbank


def delete_snowflake(n):
        point[n] = sd.get_point(list_x[n], list_y[n])
        sd.snowflake(center=point[n], color=sd.background_color, length=list_length[n])

        list_y[n] = 700
