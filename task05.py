#!/usr/bin/env python3

# задача 5
"""
Вывести английский алфавит по 5 букв в строке.
"""
for i in range(65, 91):
    print(chr(i), end=' ')
    if (i - 4) % 5 == 0:
        print()
for i in range(97, 123):
    print(chr(i), end=' ')
    if i % 5 == 0:
        print()
print()
