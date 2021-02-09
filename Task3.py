def my_func(a, b, c):
    my_list = [a, b, c]
    max_1 = max(a, b, c)
    my_list.remove(max_1)
    max_2 = max(my_list)
    result = max_1 + max_2
    return result


print(my_func(1, 10, 10))
