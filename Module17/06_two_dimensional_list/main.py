# `[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]`
import random


def list_num_fun():
    list_num = [random.randint(1, 12) for _ in range(3)]
    return list_num


list_result = [list_num_fun() for i in range(4)]
print(list_result)
