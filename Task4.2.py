def my_func():
    x = int(input('Введите действительное положительное число x: '))
    y = int(input('Введите целое отрицательное число y: '))
    y = abs(y)
    res = 1
    for i in range(y):
        res *= x
    result = 1 / (res)
    return result


print(my_func())
