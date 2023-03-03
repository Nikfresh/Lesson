# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)


from random import randint, shuffle

from termcolor import cprint


class Cat:
    def __init__(self, name):
        self.name = 'Кот ' + name
        self.fullness = 30
        self.house = House()
        self.house.name = "бездомный"
        self.live = True

    def __str__(self):
        if self.live == True:
            return f"{self.name}, сытость - {self.fullness}, живет в  - {self.house.name}"
        else:
            return f"{self.name}, СДОХ в  - {self.house.name}"

    # Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
    # Когда кот спит - сытость уменьшается на 10
    # Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
    # Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
    # Если степень сытости < 0, кот умирает.
    # Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
    # что будет делать сегодня

    def eat(self):
        if self.house.bowl >= 10:
            self.fullness += 20
            self.house.bowl -= 10
        else:
            cprint('Нет еды для кошек!!!',color='red',on_color='on_yellow')

    def act(self):
        dise = randint(1, 3)
        if self.fullness < 0:
            self.live = False
        elif dise == 1:
            self.eat()
        elif dise == 2:
            self.game()
        elif dise == 3:
            self.sleep()

    def game(self):
        self.fullness -= 10
        self.house.dirt += 5

    def sleep(self):
        self.fullness -= 10
        cprint(f'{self.name} проспал весь день.', color='yellow', )



class House:
    """Дом"""

    def __init__(self, name='бездомный'):
        self.food = 100
        self.money = 50
        self.name = name

    def __str__(self):
        return f"Дом - {self.name}, еды осталось - {self.food}, денег есть - {self.money}"


class Man:
    """ Человек"""

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = House()
        self.house.name = "бездомный"

    def buy_food_cat(self):
        self.house.money -= 50
        self.house.bowl += 50
        cprint(f'{self.name} купил кошачий корм.', color='magenta')

    def __str__(self):
        return f"Я - {self.name}, сытость - {self.fullness}, живет в  - {self.house.name}"

    def eat(self):
        if self.house.food >= 10:
            cprint(f"{self.name} вкусно поел.", color='blue')
            self.fullness += 10
            self.house.food -= 20
            return True
        else:
            cprint(f"{self.name} - хотел поесть, но обнаружил, что еда кончилась(((", color='red')
            return False

    def cleaning(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint(f'{self.name} прибрался в доме.', color='yellow', on_color='on_blue')

    def work(self):
        cprint(f"{self.name} сходил на работу", color='cyan')
        self.house.money += 150
        self.fullness -= 10

    def play_dota(self):
        cprint(f"{self.name} играл в доту весь день", color='green')
        self.fullness -= 10

    def shop_food(self):
        cprint(f"{self.name} сходил в магазин и купил еды", color='magenta')
        self.house.food += 40
        self.house.money -= 10

    def act(self):
        dise = randint(1, 6)
        if self.fullness == 0:
            print(f"{self.name} умер от переистощения")
            return
        elif self.fullness <= 10:
            if self.eat() == False:
                if self.house.money <= 20:
                    self.work()
                elif self.house.food <= 20:
                    self.shop_food()
        elif dise == 1:
            self.work()
        elif dise == 2:
            if self.eat() == False:
                if self.house.money <= 20:
                    self.work()
                elif self.house.food <= 20:
                    self.shop_food()
        elif dise == 3:
            self.buy_food_cat()
        else:
            self.play_dota()

    def go_in_house(self, home):
        if self.house.name == "бездомный":
            self.house = home
            cprint(f"{self.name} заехал в {self.house.name}", color='cyan')
            self.fullness -= 10
        else:
            cprint(f"{self.name} уже живет в {self.house.name} ему не надо заселяться снова", color='red')

    def got_a_cat(self, cat):
        if cat.house.name == "бездомный":
            cat.house = self.house
            cprint(f"{self.name} подобрал {cat.name} и поселил в {self.house.name}", color='cyan')
            self.fullness -= 10
            cat.house.bowl = 0
            cat.house.dirt = 0
        else:
            cprint(f"{self.name} уже живет в {self.house.name} ему не надо заселяться снова", color='red')


# Человеку и коту надо вместе прожить 365 дней.

citizens = [Man('Бадхед'), Man('Бивис'), Man('Егорик')]
home_for_man = House('ДОМЯРА')
for citizen in citizens:
    citizen.go_in_house(home=home_for_man)
shuffle_list_of_citizens = (list(range(0, len(citizens))))
for day in range(1, 100):
    shuffle(shuffle_list_of_citizens)
    print(f"=================День {day}=================", )
    for i in shuffle_list_of_citizens:
        citizens[i].act()
    for i in citizens:
        print(i)
    print(home_for_man)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
