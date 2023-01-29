# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
expenses_month = expenses
i = 0
money_from_parent = 0
while i < 10:
    i += 1
    money_from_parent = expenses_month-educational_grant+money_from_parent
    print('расход на месяц',i,' составляет',expenses_month-educational_grant)
    expenses_month = expenses_month*1.03
print('Студенту надо попросить',round(money_from_parent,2), 'рублей')

