

class Man:
    def __init__(self, name):
        self.cash = 100
        self.bankir = None
        self.name = name

    def cach_to_bank(self, bank):
        self.bankir = bank
        print(self.bankir , '-bank' , self.name , 'money = ' , bank.money)

class Bankir:
    def __init__(self, name):
        self.money = 500
        self.name = name

nik = Man('Nик')
bank = Bankir('BTБ')
print("nik id =", id(nik))
print('nik cahc= ', nik.cash)
print('обьект к в классе ник в методе банкир - ', nik.bankir)
print("имя класса ник - ", nik.name)
print('имя класса банк - ', bank.name)
print('деньги в банке =  ', bank.money)
nik.cach_to_bank(bank)
print('создали обьект ,Bankir ВНУТРИ ОБЪЕКТА  ник')
print(f'в обьекте {nik.name} по методу bankir.money. {nik.bankir.money} имя банка  внутри {nik.name}={nik.bankir.name}')
print(nik.bankir)
print(id(nik.bankir))
print(nik.bankir.money)
print(bank.money)
nik.bankir.money = 100000
print(nik.bankir.money)
print(bank.money)
print(id(nik.bankir.money))
print(id(bank.money))
nik2 = Man('Gocha')
nik2.cach_to_bank(bank)
print(id(nik2.bankir.money))
print(nik2.bankir.money)
nik2.bankir.money = 333

print(nik.bankir.money)