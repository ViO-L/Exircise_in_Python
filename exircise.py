'''Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.
Пример
На входе:
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7, 11]
# min_number = 0
# max_number = 10
# list_2 = []
# for i in range(len(list_1)):
#         if list_1[i] >= min_number and list_1[i] <= max_number:
#             list_2.append(i)
# for i in range(len(list_2)):
#         print(list_2[i])
'''

'''Заполните массив элементами арифметической прогрессии. Её первый элемент a1 ,

разность d и количество элементов n будет задано автоматически.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Пример
На входе:
a1 = 2
d = 3
n = 4
На выходе:
2
5
8
11
# an = a1 + (n-1) * d. an = 2 + (4 - 1) * 3
# a4 = a1 + d + d + d = 2 + 3 + 3 + 3 = 11
arith_progression = []
a1 = 2
d = 3
n = 4
for i in range(n):
    an = a1 + i * d
    arith_progression.append(an)
    print(arith_progression[i])
    print(f'это индекс{i} это {n}')
'''

'''Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию,
вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
Пример
На входе:

print_operation_table(lambda x, y: x * y, 3, 3)
На выходе:

1 2 3
2 4 6 
3 6 9
'''
def print_operation_table(operation, num_rows , num_columns):
    if num_rows <= 2 and num_columns <= 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    
    for i in range(1, num_columns + 1, 1):
        
    
    
    
    
print(print_operation_table(lambda x, y: x * y, 3, 3))