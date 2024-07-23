import random


def function(i, j):
    return i, j


new_list = []
list1 = [random.randint(0, 10) for _ in range(10)]
print(list1)
for i in range(0, 10, 2):
    new_list.append(function(list1[i], list1[i + 1]))
print(new_list)


list2 = []
list3 = []
for i in range(0, 10, 2):
    list2.append(list1[i])
    list3.append(list1[i + 1])
new_list1 = list(zip(list2, list3))
print(new_list1)
