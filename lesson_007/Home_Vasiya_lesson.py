from random import randint, shuffle

from termcolor import cprint


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
        self.house = House
        self.house.name = "бездомный"

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

    def work(self):
        cprint(f"{self.name} сходил на работу", color='cyan')
        self.house.money += 50
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
        else:
            self.play_dota()

    def go_in_house(self, home):
        if self.house.name == "бездомный":
            self.house = home
            cprint(f"{self.name} заехал в {self.house.name}", color='cyan')
            self.fullness -= 10
        else:
            cprint(f"{self.name} уже живет в {self.house.name} ему не надо заселяться снова", color='red')


citizens = [Man('Бадхед'), Man('Бивис'), Man('Егорик')]
home_for_man = House('ДОМЯРА')
for citizen in citizens:
    citizen.go_in_house(home=home_for_man)
# bivis.go_in_house(home=home_for_man)
# budhead.go_in_house(home=home_for_man)
print(list(range(1,len(citizens)+1)))
shuffle_list_of_citizens = (list(range(0,len(citizens))))
for day in range(1, 100):
    shuffle(shuffle_list_of_citizens)
    print(f"=================День {day}=================", )
    for i in shuffle_list_of_citizens:
        citizens[i].act()
    for i in citizens:
        print(i)
    print(home_for_man)
