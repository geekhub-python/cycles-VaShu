#!/usr/bin/env python3

# задача 7
"""
Начав тренировки, лыжник в первый день пробежал 10 км. Каждый следующий день он
увеличивал пробег на 10% от пробега предыдущего дня. Определите:
а) пробег лыжника за второй, третий, ..., десятый день тренировок;
б) какой суммарный путь он пробежал за первые 7 дней тренировок.
в) суммарный путь за n дней тренировок;
г) в какой день ему следует прекратить увеличивать пробег, если он не должен превышать 80 км?
"""
x = 10
s = 0
print('Day  1  = ', x)
for i in range(2, 11):
    x = x + x / 10
    if i <= 7:
        s = s + x
    print('Day ', i, ' = ', "%.2f" % x)

print('Sum for 7 days = ', "%.2f" % s)
# for N days
x = 10
s = 0
for i in range(2, int(input('n = '))+1):
    x = x + x / 10
    s = s + x
print('Sum = ',  "%.2f" % s)


def z7g():
    n = 10
    i = 1
    while n <= 80:
        n = n * 1.1
        i = i + 1
    print(i - 1)

z7g()