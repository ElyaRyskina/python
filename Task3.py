month_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_number = int(input('Введите порядковый номер месяца: '))
month_index = month_number_list.index(month_number)
if month_index == 2 or month_index == 3 or month_index == 4:
    print('Весна')
elif month_index == 5 or month_index == 6 or month_index == 7:
    print('Лето')
elif month_index == 8 or month_index == 9 or month_index == 10:
    print('Осень')
else:
    print('Зима')
