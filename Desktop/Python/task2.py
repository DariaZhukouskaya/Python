'''Задача 2. Найти сумму цифр трехзначного числа'''

num = int(input('Введите  трехзначное число: '))
num = int(num)

a1 = num // 100
a2 = num % 100 // 10
a3 = num % 10

print(a1, '+', a2, '+', a3, '=', a1 + a2 + a3)     