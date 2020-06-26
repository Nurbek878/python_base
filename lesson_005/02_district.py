# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

from district.central_street.house1 import room1 as centr_h1_r1
from district.central_street.house1 import room2 as centr_h1_r2
from district.central_street.house2 import room1 as centr_h2_r1
from district.central_street.house2 import room2 as centr_h2_r2
from district.soviet_street.house1 import room1 as soviet_h1_r1
from district.soviet_street.house1 import room2 as soviet_h1_r2
from district.soviet_street.house2 import room1 as soviet_h2_r1
from district.soviet_street.house2 import room2 as soviet_h2_r2

result =', '
print('На районе живут', result.join(centr_h1_r1.folks), result.join(centr_h1_r2.folks), '\n',
                         result.join(centr_h2_r1.folks), result.join(centr_h2_r2.folks), '\n',
                         result.join(soviet_h1_r1.folks), result.join(soviet_h1_r2.folks),'\n',
                         result.join(soviet_h2_r1.folks), result.join(soviet_h2_r2.folks))



