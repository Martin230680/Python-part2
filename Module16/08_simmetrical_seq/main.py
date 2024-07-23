import math


def input_list(N):
    list_numbers = []
    for i in range(1, N + 1):
        number = int(input(f"Введите {i} число: "))
        list_numbers.append(number)
    return list_numbers


N = int(input("Кол-во чисел: "))
list_numbers = input_list(N)
list_compare = list_numbers[:]
print("Последовательность:", list_numbers)
list_add = []
count = 1
list_add1 = []
while count <= math.ceil((N / 2)):
    list_add.append(list_numbers[count - 1])
    if list_numbers[count - 1] != list_numbers[-count]:
        list_add1 = list_add[:]
        list_add1.reverse()
        list_numbers = list_compare + list_add1
        N = len(list_numbers)
    count += 1
print("Симметричная последовательность: ", list_numbers)
print("Количество чисел: ", len(list_add1))
print("Сами числа: ", list_add1)


# while True:
#     count = 0
#     for i in range(1, math.ceil(N / 2) + 1):
#         list_add.append(list_numbers[i - 1])
#         if list_numbers[i - 1] != list_numbers[-i]:
#             list_add.reverse()
#             list_numbers = list_compare + list_add
#             N = len(list_numbers)
#             list_add = []
#             break
#         else:
#             count += 1
#     if count == math.ceil(N / 2):
#         break
# print(list_numbers )
# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 1
# Число: 2
# Число: 2
#
# Последовательность: [1, 2, 1, 2, 2]
# Нужно приписать чисел: 3
# Сами числа: [1, 2, 1]
