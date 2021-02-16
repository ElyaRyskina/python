from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]


def my_func(el_1, el_2):
    return el_1 * el_2from
    functools
    import reduce


my_list = [el for el in range(100, 1001) if el % 2 == 0]


def my_func(el_1, el_2):
    return el_1 * el_2


print(reduce(my_func, my_list))
