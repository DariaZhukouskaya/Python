'''Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
дано: 2, 2
вывод: 4'''


def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)

print(sum(2, 2))