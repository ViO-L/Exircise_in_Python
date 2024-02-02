'''У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transormed_values = list(map(lambda x : x, values))
if values == transormed_values:
    print("ok")
else:
    print("no")
print(values)
print(transormed_values)
'''
'''Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна

Решение 1
def squer_orbits(r1, r2):
    return math.pi * r1 * r2

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

filtered_orbits = list(filter(lambda x: x[0] != x[1], orbits))
max_orbit = max(list(map(lambda a: squer_orbits(a[0], a[1]), filtered_orbits)))
result = list(filter(lambda a: max_orbit == squer_orbits(a[0], a[1]), orbits))

print(filtered_orbits)

print(max_orbit)

print(*result[0])

Решение 2
def find_farthest_orbit(orbit_list):
    #создаем новый список из введенного
    #map() итерирует каждый элемент введеного списка, а это кортеж
    #lambda(x) если элементы кортежа не равны - умножает
    orbits_multiplay = list(map(lambda x: x[0]*x[1]*3.14 if x[0]!= x[1] else -1, orbit_list))
    #определяем индекс максимальногшо элемента в новом списке
    max_element_index = orbits_multiplay.index(map(orbits_multiplay))
    return orbits[max_element_index]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
'''
'''Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.

def same_by(characteristic, objects):
    list1 = list(map(characteristic, objects))
    list2 = list(filter(lambda x: x ==False, list1))
    if len(list2) == 0:
        print('same')
    else:
    print('not the same')

def same_by2(characteristic, objects):
    if len(objects) == 0: return True
    temp = characteristic(objects[0])
    list1 = list(map(lambda x: characteristic(x) == temp, objects))
# print(list1)
# print(all(list1))
# print(any(list1))
    return all(list1)


values = [0, 2, 10, 8, '4']
values2 = ['жираф', 'слон', 234]
values3 = ()

sample1 = lambda x: x % 2 == 0 # Четность
sample2 = lambda x: x >= 0 # Неотрицательное число
sample3 = lambda x: isinstance(x, str) # Строковый тип
sample4 = lambda x: isinstance(x, int) # Целочисленный тип
sample5 = lambda x: x is None #Пустое множество


print(same_by2(sample3, values2))

'''