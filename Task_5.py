proceeds = int(input('Введите сумму выручки: '))
cost = int(input('Введите сумму издержек: '))
if proceeds > cost:
    print('Фирма работает с прибылью')
    profit = (proceeds - cost) / proceeds
    print('Рентабельность: ', profit)
    numbers_emp = int(input('Введите численность сотрудников: '))
    print('Прибыль фирмы в расчете на одного сотрудника: ', (proceeds - cost) / numbers_emp)
elif proceeds == cost:
    print('Прибыли нет, убытка тоже. Фирма работает в ноль')
else:
    print('Фирма работает с убытком')
