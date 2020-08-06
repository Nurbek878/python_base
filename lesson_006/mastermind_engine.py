from random import randint


def pick_number():
    pick = []
    for i in range(10):
        n = randint(1, 9)
        if not (n in pick):
            pick.append(n)
        if len(pick) == 4:
            break
    return pick


def check_input(num):
    global control
    control = None
    if len(num) != len(set(num)):
        control = 1
        print("Вы ввели число, не все цифры которого различны")
    return control



def check_number(num, hidden_num):
    result = {'bulls': 0, 'cows': 0}
    global bulls, cows
    bulls = None
    cows = None
    num_list = list(map(int, list(num)))
    hidden_num_list = list(map(int, list(hidden_num)))

    for i in range(4):
        if num_list[i] == hidden_num_list[i]:
            result['bulls'] += 1
        else:
            if num_list[i] in hidden_num_list:
                result['cows'] += 1

    return result
