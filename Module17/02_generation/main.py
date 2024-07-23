import math

N = int(input("Введите длину списка: "))
num_list = [1 if i % 2 == 0 else math.ceil(i % 5) for i in range(N)]
print("Результат: ", num_list)
