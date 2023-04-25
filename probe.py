'''class Man:
    def __init__(self, name):
        self.cash = [333]
        self.bankir = None
        self.name = name

    def invite_bank(self, bank):
        self.bankir = bank
        self.cach_merge_bank_money(bank)
        print(self.bankir, '-bank', self.name, 'money = ', bank.money)

    def cach_merge_bank_money(self, bank):
        self.cash = self.bankir.money = bank.money


class Bankir:
    def __init__(self, name):
        self.money = [999]
        self.name = name


nik = Man('Nикита')
nik2 = Man('Gocha')
bank = Bankir('BTБ')
# print("nik id =", id(nik))
# print('nik cahc= ', nik.cash)
# print('обьект к в классе ник в методе банкир - ', nik.bankir)
# print("имя класса ник - ", nik.name)
# print('имя класса банк - ', bank.name)
# print('деньги в банке =  ', bank.money)
nik.invite_bank(bank)
nik2.invite_bank(bank)
# print('создали обьект ,Bankir ВНУТРИ ОБЪЕКТА  ник')
# print(f'в обьекте {nik.name} по методу bankir.money. {nik.bankir.money} имя банка  внутри {nik.name}={nik.bankir.name}')
print('id nik.bankir.money'.ljust(25), id(nik.bankir.money))
print('id nik2.bankir.money'.ljust(25), id(nik2.bankir.money))
print('id bank.money'.ljust(25), id(bank.money))
print('id nik.cash'.ljust(25), id(nik.cash))
print('id nik2.cash'.ljust(25), id(nik2.cash))
print('nik.bankir.money = '.ljust(25), nik.bankir.money)
print('bank.money = '.ljust(25), bank.money)
print('nik.cash = '.ljust(25), nik.cash)
print('nik2.cash = '.ljust(25), nik2.cash)
print('nik2.bankir.money = '.ljust(25), nik2.bankir.money)
print('смотрим как связались методы кэш в ник и моней в банке')
print(f'id cach-{nik.name}={id(nik.cash)}')
print(f'id cach-{nik2.name} ={id(nik2.cash)}')
print(f'id money-{bank.name}  ={id(bank.money)}')
nik.cash = nik2.cash = bank.money
bank.money = [555]
nik.cash = 222
nik.cash = nik2.cash = bank.money
print('\nизменили bank.money на [555]\n')
print('id nik.bankir.money'.ljust(25), id(nik.bankir.money))
print('id nik2.bankir.money'.ljust(25), id(nik2.bankir.money))
print('id bank.money'.ljust(25), id(bank.money))
print('id nik.cash'.ljust(25), id(nik.cash))
print('id nik2.cash'.ljust(25), id(nik2.cash))
print('nik.bankir.money = '.ljust(25), nik.bankir.money)
print('bank.money = '.ljust(25), bank.money)
print('nik.cash = '.ljust(25), nik.cash)
print('nik2.cash = '.ljust(25), nik2.cash)
print('nik2.bankir.money = '.ljust(25), nik2.bankir.money)
print('смотрим как связались методы кэш в ник и моней в банке')
print(f'id cach-{nik.name}={id(nik.cash)}')
print(f'id cach-{nik2.name} ={id(nik2.cash)}')
print(f'id money-{bank.name}  ={id(bank.money)}')
'''
line = 'asdofin qirubsaдоышо шг т Ы ЫАЫВВЫКПЫП У '
add = {}
y = 1
for x in line:
    add[x] = len(line) + y
    y += 1
print(add)
