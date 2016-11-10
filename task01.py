#!/usr/bin/env python3

# задание 01
"""
Выведите на экран n раз фразу "Silence is golden". Число n вводит пользователь.
"""
n = int(input('Введите число повторов = '))
line_text = 'Silence is golden'

for i in range(n):
    print(line_text)
# or
j = 1
while j <= n:
    print(line_text)
    j += 1
# or
print((line_text + "\n") * n)