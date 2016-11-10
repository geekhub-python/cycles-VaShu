#!/usr/bin/env python3

# задача 3
"""
Найти произведение `5 * 6 * 7 * ... * 13`.
"""
a = 5
for i in range(6, 13):
    a = a * i
#    print(a, end=' ')
print(a, end=' ')
