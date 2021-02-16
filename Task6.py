from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

i = 0
for el in cycle(range(3)):
    if i > 10:
        break
    print(el)
    i += 1
