# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код

from room_1 import folks as room_1_folks
from room_2 import folks as room_2_folks
result =' '
print('В комнате room_1 живут:', result.join(room_1_folks))
print('В комнате room_2 живут:', result.join(room_2_folks))
