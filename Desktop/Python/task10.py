'''На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - 
определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.
coins = [0, 1, 0, 1, 1, 0]'''

coins = [0, 1, 0, 1, 1, 0]
a = 0 # создали a и b это счетчики
b = 0

for i in coins:  
    if i == 0:   # если i = 0
        a += 1   # увеличиваем a на 1
    else:
        b += 1   # увеличиваем b на 1
if a < b:        
    print(a)
else:
    print(b)