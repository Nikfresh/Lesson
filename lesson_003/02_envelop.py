# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные
def check_paper_in_evenlop(evenlop_x, evenlop_y, paper_x, paper_y):
    print('Конверт', evenlop_x, 'на', evenlop_y)
    if paper_x <= envelop_x and paper_y <= envelop_y:
        print('Лист помещается - ', paper_x, 'на', paper_y)
    elif paper_x <= envelop_y and paper_y <= envelop_x:
        print('Лист помещается повернутым', paper_y, 'на', paper_x)
    else:
        print('Лист не помещается', paper_x, 'на', paper_y)
    input()


def check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z):
    print('Дыра с размерами- ', hole_x, 'на', hole_y)
    print('Кирпич', brick_x, 'на', brick_y, 'на', brick_z)
    if brick_x <= hole_x and brick_y <= hole_y:
        print('Ккирпич входит в дыру по сторонам', brick_x, 'на', brick_y)
    elif brick_y <= hole_x and brick_x <= hole_y:
        print('Ккирпич входит в дыру по сторонам', brick_y, 'на', brick_x)
    elif brick_x <= hole_x and brick_z <= hole_y:
        print('Ккирпич входит в дыру по сторонам', brick_x, 'на', brick_z)
    elif brick_z <= hole_x and brick_x <= hole_y:
        print('Ккирпич входит в дыру по сторонам', brick_z, 'на', brick_x)
    elif brick_y <= hole_x and brick_z <= hole_y:
        print('Ккирпич входит в дыру по сторонам', brick_y, 'на', brick_z)
    elif brick_z <= hole_x and brick_y <= hole_y:
        print('Ккирпич входит в дыру по сторонам', brick_z, 'на', brick_y)
    else:
        print('Кирпич не входит как ни крути(((')
        print()
    input('Enter для следующего кирпича')
    print()


'''
print("Привет")
envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
check_paper_in_evenlop(envelop_x, envelop_y, paper_x, paper_y)
# проверить для
paper_x, paper_y = 9, 8
check_paper_in_evenlop(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 6, 8
check_paper_in_evenlop(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 8, 6
check_paper_in_evenlop(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 3, 4
check_paper_in_evenlop(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 11, 9
check_paper_in_evenlop(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 9, 11
check_paper_in_evenlop(envelop_x, envelop_y, paper_x, paper_y)
# (просто раскоментировать нужную строку и проверить свой код)


print('Пока')'''

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 2, 10
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 10, 11, 2
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 10, 2, 11
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 2, 10, 11
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 2, 11, 10
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 5, 6
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 6, 5
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 3, 5
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 5, 3
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 5, 6, 3
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 5, 3, 6
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 3, 6
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 6, 3
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 11, 3
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 3, 11
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 6, 11
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 11, 6
check_brick_to_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
# (просто раскоментировать нужную строку и проверить свой код)


