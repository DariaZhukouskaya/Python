'''Задача №45.
Два различных натуральных числа n и m называютсядружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m инаоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественныхчисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, непревосходящее 105. Программа должна вывести все
пары дружественных чисел, каждое из которых непревосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна бытьвыведена только один раз (перестановка чисел новую
пару не дает).
Ввод: 300 
Вывод: 220: 284'''


n = 300
dict = {1: 1}
for i in range(n):
    x = i - 1
    sum = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            sum += j
    dict[i] = sum

print(dict)

# дописать!