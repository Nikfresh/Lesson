# -*- coding: utf-8 -*-

# Есть файл calc.txt с записями операций - текстовый калькулятор. Записи вида
#
# 100 + 34
# 23 / 4
#
# то есть ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделенные пробелами.
# Операндны - целые числа. Операции - арифметические, целочисленное деление и остаток от деления.
#
# Нужно вычислить все операции и найти сумму их результата.

def calculate(line):
    operand1, operation, operand2 = line[:-1].split(sep=' ')
    operand1, operand2 = int(operand1), int(operand2)
    if operation == '+':
        result = operand1 + operand2
    elif operation == '-':
        result = operand1 - operand2
    elif operation == '*':
        result = operand1 * operand2
    elif operation == '/':
        result = operand1 / operand2
    elif operation == '//':
        result = operand1 // operand2
    elif operation == '%':
        result = operand1 % operand2
    else:
        print('Uncnow operand')
    return result

total = 0
with open('calc.txt', 'r') as ff:
    for line in ff:
        try:
            total += calculate(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'не хватает операнда"{line[:-1]}" ошибка {exc}')
            else:
                print(f'не преобразуемая строка"{line[:-1]}" ошибка {exc}')
print(f'Total = {total}')

'''def calc(line):
    # print(f'Read line {line}', flush=True)
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        value = operand_1 + operand_2
    elif operation == '-':
        value = operand_1 - operand_2
    elif operation == '/':
        value = operand_1 / operand_2
    elif operation == '*':
        value = operand_1 / operand_2
    elif operation == '//':
        value = operand_1 // operand_2
    elif operation == '%':
        value = operand_1 % operand_2
    else:
        raise ValueError('Unknown operation {operation}')
    return value


total = 0
with open('calc.txt', 'r') as ff:
    for line in ff:
        line = line[:-1]
        try:
            total += calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Не хватает операндов {exc} в строке {line}')
            else:
                print(f'Не могу преобразовать к целому {exc} в строке {line}')

print(f'Total {total}')
'''
