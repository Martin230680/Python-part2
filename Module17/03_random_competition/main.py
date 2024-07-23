import random

point_list1 = [round(random.uniform(1, 5), 2) for _ in range(20)]
point_list2 = [round(random.uniform(1, 5), 2) for _ in range(20)]
win_list = [
    point_list1[i] if point_list1[i] > point_list2[i] else point_list2[i]
    for i in range(20)
]
print("Первая команда: ", point_list1)
print("Вторая команда: ", point_list2)
print("Победители тура: ", win_list)
