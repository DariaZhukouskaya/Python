'''Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
n = 385916 -> yes
n = 123456 -> no'''

n = int(input('Введите шестизначное число: '))

n1 = n // 100000           # находим первую цифру
n2 = (n % 100000) // 10000 # находим вторую цифру
n3 = (n % 10000) // 1000
n4 = (n % 1000) // 100
n5 = (n % 100) // 10      # находим предпоследнюю цифру
n6 = n % 10               # находим последнюю цифру

if n1 + n2 + n3 == n4 + n5 + n6:
    print('yes')
else:
    print('no')

# Строковый метод:
#     x = 989989
# print(x)
# x1 = str(x)
# print(type(x), type(x1))
# print(x1[0],x1[3])

# print(int(x1[0])+int(x1[1])+int(x1[2])==int(x1[-3])+int(x1[-1])+int(x1[-2]))