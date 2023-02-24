from random import randint

from termcolor import cprint


class House:
    """Дом"""

    def __init__(self):
        self.food = 10
        self.money = 100000
        self.name = 'Домищще'

    def __str__(self):
        return f"Дом - {self.name}, еды осталось - {self.food}, денег есть - {self.money}"


class Man:
    """ Человек"""

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 40
        self.money = 30
        self.house = House
        self.house.name = "бездомный"

    def __str__(self):
        return f"Я - {self.name}, сытость - {self.fullness}, еды осталось - {self.food}, денег есть - {self.money}, живет в  - {self.house.name}"

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
            print(f"{self.name} умер от переистощения")
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

    def go_in_house(self, home):
        if self.house.name == "бездомный":
            self.house = home
            print(f"{self.name} заехал в {self.house.name}")
            self.fullness -= 10
            self.house.money += self.money
            self.money = home.money
        else: cprint(f"{self.name} уже живет в {self.house.name} ему не надо заселяться снова",color='red')


bivis = Man('Бивис')
budhead = Man('Бадхед')
home_for_man = House()
# print(bivis)
# bivis.go_in_house(home=home_for_man)
# print(bivis)
# print(home_for_man)
day_of_bivis_go_house = 3 #randint(3,10)
day_of_budhead_go_house = 4#randint(3,10)
for day in range(1, 10):
    print(f"=================День {day}=================", )
    bivis.act()
    budhead.act()
    print(bivis)
    print(budhead)
    print(home_for_man)
    if day == day_of_bivis_go_house:
        bivis.go_in_house(home=home_for_man)
    if day == day_of_budhead_go_house:
        budhead.go_in_house(home=home_for_man)
