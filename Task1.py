def func_del(number_1, number_2):
    if number_2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(number_1 / number_2)


num_1 = int(input('Введите делимое: '))
num_2 = int(input('Введите делитель: '))
func_del(num_1, num_2)
