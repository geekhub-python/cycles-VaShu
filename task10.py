#!/usr/bin/env python3

# задача 10
"""
Сгенерировать пароль для пользователя. Требования: длина от 6 до 20 символов,
должен быть ровно один символ подчеркивания, хотя бы две заглавные буквы, не
более 5 цифр. Любые две цифры подряд недопустимы.
"""
import random

def az10():
    dl = 0
    dl1 = 0
    dl2 = 0
    dl3 = 0
    l1 = ['_']
    l2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W',
          'X', 'Y', 'Z', 'Q']
    l3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    l = []
    l_ = ''
    l_s = ''
    dl = random.randint(7, 20)
    dl1 = 1
    dl3 = random.randint(1, 5)
    dl2 = dl - dl1 - dl3
    i = 1
    l.append(l1[0])
    while i <= dl2:
        el = random.choice(l2)
        l.append(el)
        i = i + 1
    i = 1
    while i <= dl3:
        el = random.choice(l3)
        i1 = l_s.find(el)
        if i1 < 0:
            l.append(el)
            l_s = l_s + el
            i = i + 1
    random.shuffle(l)
    print(l)
    print(l_.join(l))

az10()
