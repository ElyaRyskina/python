my_list = input('Введите слова через пробел: ').split()
for ind, el in enumerate(my_list, 1):
    if len(el) > 10:
        el = el[0:10]
    print(ind, el)
