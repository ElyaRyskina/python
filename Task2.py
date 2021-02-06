my_list_1 = input('Введите элементы списка через пробел').split()
if len(my_list_1) % 2 == 0:
    n = len(my_list_1)
else:
    n = len(my_list_1) - 1
for el in range(0, n - 1, 2):
    my_list_1[el], my_list_1[el + 1] = my_list_1[el + 1], my_list_1[el]
print(my_list_1)
