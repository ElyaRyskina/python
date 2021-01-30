time = int(input('Введите время в секундах: '))
time_hour = time // 3600
time_minute = (time - (time_hour * 3600)) // 60
time_second = (time - (time_hour * 3600) - (time_minute * 60))
print(f'{time_hour:02d}:{time_minute:02d}:{time_second:02d}')
