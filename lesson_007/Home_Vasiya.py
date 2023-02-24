from random import randint

from termcolor import cprint


class Man:
    """ Человек"""

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 40
        self.money = 30

    def __str__(self):
        return f"Я - {self.name}, сытость - {self.fullness}, еды осталось - {self.food}, денег есть - {self.money}"

    def eat(self):
        if self.food >= 10:
            cprint(f"{self.name} вкусно поел.", color='blue')
            self.fullness += 10
            self.food -= 20
        else:
            cprint(f"{self.name} - нет еды(", color='red')

    def work(self):
        print(f"{self.name} сходил на работу")
        self.money += 50
        self.fullness -= 10

    def play_dota(self):
        cprint(f"{self.name} играл в доту весь день", color='green')
        self.fullness -= 10

    def shop_food(self):
        cprint(f"{self.name} сходил в магазин и купил еды", color='magenta')
        self.food += 40
        self.money -= 10

    def act(self):
        dise = randint(1, 6)
        if self.fullness < 5:
            print(f"{self.name} умер от переистощения" )
            return
        if self.money <= 20:
            self.work()
        elif self.food <= 20:
            self.shop_food()
        elif self.fullness <= 20:
            self.eat()

        elif dise == 1:
            self.work()
        elif dise == 2:
            self.eat()
        else:
            self.play_dota()


vasya = Man('Вася')

for day in range(1, 366):
    print(f"=================День {day}=================", )
    vasya.act()
    print(vasya)


