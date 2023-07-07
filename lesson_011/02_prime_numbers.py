# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         if i <= n
#             for prime in prime_numbers:
#                 if number % prime == 0:
#                     break
#             else:
#                 prime_numbers.append(number)
#     return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n=100):
        self.n = n
        self.i = 1

    def __iter__(self):
        self.prime_numbers = []
        self.i = 1
        return self

    def __next__(self):
        while True:
            self.i += 1
            for prime in self.prime_numbers:
                if self.i % prime == 0:
                    break
            else:
                self.prime_numbers.append(self.i)
                return self.i
            if self.i >= self.n:
                raise StopIteration()

    def __call__(self, n):
        return self

    def sum_lucky(list):
        sum_right, sum_left = 0, 0
        len_list = len(list) // 2
        for i in range(len_list):
            sum_left += list[i]
            sum_right = sum_right + list.pop()
        if sum_right == sum_left:
            return True
        else:
            return False

    def lucky(num):
        list_num = [int(i) for i in str(num)]
        if len(list_num) >= 2 and sum_lucky(list_num):
            return True
        return False

    def check_polindrom(list):
        begin_num = list.pop(0)
        end_num = list.pop()
        if begin_num == end_num:
            if len(list) >= 2:
                return check_polindrom(list)
            return True
        return False

    def polindrom(num):
        list_num = [int(i) for i in str(num)]
        if len(list_num) >= 2 and check_polindrom(list_num):
            return True
        return False


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик

def prime_numbers_generator(inc):
    prime_number_iterator = PrimeNumbers(inc)
    return prime_number_iterator





for number in prime_numbers_generator(inc=100000):
    # if lucky(number):
    #     print(f'{number} счастливое число')
    if polindrom(number):
        print(f'{number} полиндром ')

    # Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
