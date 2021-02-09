def my_func():
    summa = 0
    try:
        while True:
            for i in map(int, input().split()):
                summa += i
            print(summa)
    except ValueError:
        print(summa)


print(my_func())
