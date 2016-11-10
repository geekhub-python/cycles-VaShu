#!/usr/bin/env python3

# задача 4

"""
Найдите хотя бы одно натуральное число, которое делится на 11, а
при делении на `2, 3, 4, ..., 10` дает в остатке 1.
"""


# from itertools import combinations as cmb
# print(sum(1 for x in cmb(map(int, input().split()), 2) if x[0]==x[1]))

def az4():
    n = 0
    q = 1
    while q >= 1:
        n = n + 1
        if n % 11 == 0:
            if (n % 2 == 1 and
                            n % 3 == 1 and
                            n % 4 == 1 and
                            n % 5 == 1 and
                            n % 6 == 1 and
                            n % 7 == 1 and
                            n % 8 == 1 and
                            n % 9 == 1 and
                            n % 10 == 1):
                print(n)
                q = 0


az4()
# 25201
