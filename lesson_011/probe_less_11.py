#
# Создадим генератор очереди
def queue(*args):
    data = list(args)
    while data:
        next = data.pop(0)
        new_value = (yield next)
        # обратите внимание, что yield возвращает значение и скобки
        if new_value is not None:
            data.append(new_value)


shop_queue = queue('Вася', 'Марина', 'Владислав', 'Эльвира')
for name in shop_queue:
    print(f'К кассе приглашается {name}')
    if name == 'Марина':
        print('А кто последний?')
        name = shop_queue.send('Маргарита Иванна')
        print(f'К кассе приглашается {name}')


# Такие генераторы называются сопрограммами (coroutines)
# - они могут как отдавать значения, так и получать.
# И хранят свое состояние. Сопрограммы можно передавать в качестве параметров в другие функции
# и устраивать цепочки обработки.
# Вот пример промышленного использования сопрограмм https://goo.gl/SHAPNk

