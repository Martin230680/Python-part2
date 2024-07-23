# import random
# str_1 = input('Введите cстроку: ')
# list_1 = [random.randint(10, 50) for _ in range(len(str_1))]
# tpl_1 = tuple(list_1)
# print('Строка: ',str_1)
# print('Кортеж чисел: ', tpl_1)
# print()
# zipp = zip(str_1, tpl_1)
# print('Результат: ', zipp)
# for i in zipp:
#     print(i)

import random

str_1 = input("Введите строку: ")
list_1 = [random.randint(10, 50) for _ in range(len(str_1))]
tpl_1 = tuple(list_1)
print("Строка: ", str_1)
print("Кортеж чисел: ", tpl_1)
print()
pairs = ((str_1[i], tpl_1[i]) for i in range(len(str_1)))
print(pairs)
for i in pairs:
    print(i)
