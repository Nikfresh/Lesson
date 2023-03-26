# -*- coding: utf-8 -*-

from termcolor import cprint, colored
from random import randint, choice


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self, name='Дом'):
        self.name = name
        self.food = 50
        self.food_pet = 30
        self.money = 100
        self.mud = 0
        self.residents = []
        self.pets = []

    def __str__(self):
        residents = ''
        for i in range(0, len(self.residents)):
            residents += ' ' + self.residents[i].name
        return colored(
            f'{self.name} еда {self.food} еда кота {self.food_pet} грязь {self.mud} деньги {self.money} жители{residents}',
            color='yellow')

    def act(self):
        if self.mud > 90:
            cprint(f'В доме грязно, у всех падает счастье.', color='red')
            for i in range(0, len(self.residents)):
                self.residents[i].happiness -= 10
        self.mud += 5


class Life_form:
    all_food_eating = 0
    all_money_off = 0
    all_money_wokr = 0

    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.fullness = 30
        self.happiness = 100
        self.status = 1
        self.home.residents.append(self)

    def __str__(self):
        return colored(f'{self.name} сытость {self.fullness} счастье {self.happiness}', color='yellow')

    def eat(self, max_eat=30, multiply=1):
        if isinstance(self, Cat):
            if self.home.food_pet <= 0:
                cprint(f'{self.name} хочет поесть но еды нет ', color='red')
                self.status = 0 if self.fullness <= 0 else 1
                return False
        if self.home.food <= 0:
            cprint(f'{self.name} хочет поесть но еды нет ', color='red')
            self.status = 0 if self.fullness <= 0 else 1
            return False
        if isinstance(self, Cat):
            food_pet_house = self.home.food_pet
            food = randint(max_eat / 2, max_eat) if food_pet_house >= max_eat else food_pet_house
            self.fullness += food * multiply
            self.home.food_pet -= food
            cprint(f'{self.name} поел(а) {food} еды', color='green')
            Life_form.all_food_eating += food
            return True
        food_house = self.home.food
        food = randint(max_eat / 2, max_eat) if food_house >= max_eat else food_house
        self.fullness += food
        self.home.food -= food
        Life_form.all_food_eating += food
        cprint(f'{self.name} поел(а) {food} еды', color='green')
        return True


class Husband(Life_form):

    def shopping_cat(self):
        if self.home.money <= 0:
            cprint(f'{self.name} хотел сходить в магазин за едой для кота но денег нет, пошел работать')
            self.work()
            return
        food = randint(100, 200)
        self.fullness -= 10
        if self.home.money <= food:
            food = self.home.money
        self.home.money -= food
        self.home.food_pet += food
        Life_form.all_money_off += food

        cprint(f'{self.name} сходил в магазин купил {food} еды для кота', color='cyan')

    def work(self):
        self.fullness -= 10
        self.home.money += 150
        Life_form.all_money_wokr += 150
        cprint(f'{self.name} сходил на работу', color='blue')

    def caress_cat(self):
        self.happiness += 5
        self.fullness -= 10
        cprint(f'{self.name} весь день гладила кота и наслаждался', color='yellow')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint(f'{self.name} поиграл в Танки', color='cyan')

    def act(self):
        rand = randint(1, 6)
        if self.status == 0:
            cprint(f'{self.name}  - !!!ТРУП!!!', color="red", attrs=['reverse'])
            return
        if self.fullness < 11:
            eating = self.eat()
            if not eating:
                self.gaming()

        elif self.home.money < 30:
            self.work()
        elif self.happiness < 10:
            self.gaming()
        else:
            if rand == 1:
                self.eat()
            elif rand == 2:
                self.work()
            elif rand == 3:
                self.shopping_cat()
            elif rand == 4:
                self.caress_cat()
            elif rand > 4:
                self.gaming()
        if self.fullness <= 0 or self.happiness < 10:
            self.status = 0


class Wife(Life_form):

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint(f'{self.name} поиграла в Танки', color='cyan')

    def shopping_cat(self):
        if self.home.money <= 0:
            cprint(f'{self.name} хотела сходить в магазин за едой для кота но денег нет, наелась с горя')
            self.eat()
            return
        food = randint(100, 200)
        self.fullness -= 10
        if self.home.money <= food:
            food = self.home.money
        self.home.money -= food
        self.home.food_pet += food
        Life_form.all_money_off += food
        cprint(f'{self.name} сходила в магазин купила {food} еды для кота', color='cyan')

    def caress_cat(self):
        self.happiness += 5
        self.fullness -= 10
        cprint(f'{self.name} весь день гладила кота и наслаждалась', color='green')

    def shopping(self):
        if self.home.money <= 0:
            cprint(f'{self.name} хотела сходить в магазин за едой но денег нет, наелась с горя')
            self.eat()
            return
        food = randint(100, 200)
        self.fullness -= 10
        if self.home.money <= food:
            food = self.home.money
        self.home.money -= food
        self.home.food += food
        Life_form.all_money_off += food
        cprint(f'{self.name} сходила в магазин купила {food} еды', color='cyan')

    def buy_fur_coat(self):
        if self.home.money > 350:
            self.fullness -= 10
            self.happiness += 60
            self.home.money -= 350
            Life_form.all_money_off += 350
            cprint(f'{self.name} сходила в магазин купила шубу', color='cyan')
        else:
            cprint(f'{self.name} очень хочет повеселиться и купить шубу но денег нет и с горя весь день гладила кота',
                   color='red')
            self.caress_cat()

    def clean_house(self):
        mud = randint(50, 100)
        self.fullness -= 10
        self.home.mud = self.home.mud - mud if mud < self.home.mud else 0
        cprint(f'{self.name} прибралась дома', color='cyan')

    def act(self):
        rand = randint(1, 7)
        if self.status == 0:
            cprint(f'{self.name}  - !!!ТРУП!!!', color="red", attrs=['reverse'])
            return
        if self.fullness < 11:
            eating = self.eat()
            if not eating:
                self.act()
        elif self.home.food < 30:
            self.shopping()
        elif self.home.food_pet < 10:
            self.shopping_cat()
        elif self.home.mud > 90:
            self.clean_house()
        elif self.happiness <= 10:
            self.buy_fur_coat()
        else:
            if rand == 1:
                self.shopping()
            elif rand == 2:
                self.clean_house()
            elif rand == 3:
                self.buy_fur_coat()
            elif rand == 4:
                self.eat()
            elif rand == 5:
                self.shopping_cat()
            elif rand > 5:
                self.caress_cat()
        if self.fullness <= 0 or self.happiness < 10:
            self.status = 0


class Cat(Life_form):
    def __init__(self, name, home):
        super().__init__(name, home)
        self.home.pets.append(self)

    def act(self):
        rand = randint(1, 3)
        if self.status == 0:
            cprint(f'{self.name}  - !!!ТРУП!!!', color="red", attrs=['reverse'])
            return
        if self.fullness < 11:
            eating = self.eat()
            if not eating:
                self.sleep()
        else:
            if rand == 1:
                self.sleep()
            elif rand == 2:
                self.soil()
            elif rand == 3:
                self.eat()
        if self.fullness <= 0 or self.happiness < 10:
            self.status = 0

    # def eat(self):
    #     pass

    def sleep(self):
        self.fullness -= 10
        cprint(f'{self.name} спал весь день', attrs=['reverse'])

    def soil(self):
        self.home.mud += 5
        self.fullness -= 10
        self.happiness += 10
        cprint(f'{self.name} драл обои', color='cyan')

class Child(Life_form):

    def __init__(self, name, home):
        super().__init__(name, home)
        self.happiness = 100

    # def __str__(self):
    #     return super().__str__()

    def act(self):
        self.happiness = 100
        rand = randint(0, 1)
        if self.status == 0:
            cprint(f'{self.name}  - !!!ТРУП!!!', color="red", attrs=['reverse'])
            return
        if self.fullness < 20:
            self.eat()
        if rand == 0:
            self.sleep()
        if rand == 1:
            self.eat()
        if self.fullness <= 0 or self.happiness < 10:
            self.status = 0

    def eat(self):
        super().eat(max_eat=10, multiply=1)

    def sleep(self):
        cprint(f'{self.name} проспал весь день')
def who_dead(home):
    if isinstance(home, House):
        for i in range(0, len(home.residents)):
            resident = home.residents[i]
            if resident.status == 0:
                print('dead')
                return True

        return False
    else:
        return False


home = House()
serge = Husband(name='Сережа', home=home)
print(serge)
masha = Wife(name='Маша', home=home)
print(masha)
print(home)
print(cat)

# """
for day in range(1, 365):
    if who_dead(home):
        cprint('_________________мертвяк в доме________________', color='yellow', attrs=['reverse'])
        break
child = Child(name='Вовчик', home=home)
print(child)
print(home)

# """
for day in range(1, 365):
    if who_dead(home):
        cprint('_________________мертвяк в доме________________', color='yellow', attrs=['reverse'])
        break
    cprint('================== День {} =================='.format(day), color='red')
    home.act()
    cat.act()
    serge.act()
    masha.act()
    child.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(cat, color='cyan')
    cprint(child, color='cyan')
    cprint(home, color='cyan')


cprint(f'{Life_form.all_food_eating} съели всего еды')
cprint(f'{Life_form.all_money_off} потрачено денег всего в магазине')
cprint(f'{Life_form.all_money_wokr} заработано денег всего на работе')
"""
# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

"""
