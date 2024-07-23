# TODO здесь писать код

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [7, 14, 3, 18.5, 21, 10, 9, 6]


def isceloe(x):
    return x % 1 == 0


N = len(numbers_list)
while N > 0:
    x = isceloe(numbers_list[N - 1])
    if x:
        if numbers_list[N - 1] % 2 == 0:
            print(numbers_list[N - 1], end=" ")
    N -= 1
