quantity = int(input('Введите количество наименований: '))
name_list = []
coast_list = []
quant_list = []
unit_list = []
for el in range(quantity):
    my_string = input('Введите через пробел название, цену, количество, единицу измерения: ').split()
    name = my_string[0]
    coast = my_string[1]
    quant = my_string[2]
    unit = my_string[3]
    name_list.append(name)
    coast_list.append(coast)
    quant_list.append(quant)
    unit_list.append(unit)
analitic_dict = {'название': name_list, 'цена': coast_list, 'количество': quant_list, 'ед.': unit_list}
print(analitic_dict)
