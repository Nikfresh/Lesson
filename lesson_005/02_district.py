# -*- coding: utf-8 -*-
from pprint import pprint

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
names = []
from district .soviet_street.house1 import room1 as mans
for i in mans.folks:
    names.append(i)
from district .soviet_street.house1 import room2 as mans
for i in mans.folks:
    names.append(i)
from district .soviet_street.house2 import room1 as mans
for i in mans.folks:
    names.append(i)
from district .soviet_street.house2 import room2 as mans
for i in mans.folks:
    names.append(i)
from district .central_street.house1 import room1 as mans
for i in mans.folks:
    names.append(i)
from district .central_street.house1 import room2 as mans
for i in mans.folks:
    names.append(i)
from district .central_street.house2 import room1 as mans
for i in mans.folks:
    names.append(i)
from district .central_street.house2 import room2 as mans
for i in mans.folks:
    names.append(i)
names = ','.join(names)
pprint(names)

