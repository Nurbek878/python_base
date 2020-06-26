# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

# TODO здесь ваш код

import my_burger as mb

print('Рецепт двойного чизбургера такой:')
mb.bun()
mb.mayonnaise()
mb.cutlet()
mb.cheese()
mb.cutlet()
mb.cheese()
mb.cucumber()
mb.tomato()
mb.mayonnaise()
mb.bun()


print('\nРецепт своего бургера:')
mb.bun()
mb.mayonnaise()
mb.cutlet()
mb.cheese()
mb.cutlet()
mb.cheese()
mb.cucumber()
mb.tomato()
mb.mayonnaise()
mb.bun()
mb.salad()

