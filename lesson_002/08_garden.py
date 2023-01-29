#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = {garden[0],garden[1],garden[2],garden[3],garden[4],garden[5],garden[6]}
meadow_set = {meadow[0],meadow[1],meadow[2],meadow[3],meadow[4],meadow[5],meadow[6]}
all = garden_set | meadow_set

# выведите на консоль все виды цветов
print(all)

# выведите на консоль те, которые растут и там и там
print(garden_set & meadow_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
print(garden_set - meadow_set)

# выведите на консоль те, которые растут на лугу, но не растут в саду
print( meadow_set - garden_set)


