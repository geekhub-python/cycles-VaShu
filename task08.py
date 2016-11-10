#!/usr/bin/env python3

# задача 8
"""
Вывести на экран числа от 1000 до 9999, у которых среди цифр нет цифры 5 и цифры 6.
"""
for i in range(1000, 9999):
    if ('5' in set(str(i)) or '6' in set(str(i))) is False:
        print(i)

# two

del56 = set('56')
print([i for i in range(1000, 9999) if set(str(i)) & del56 == set()])
