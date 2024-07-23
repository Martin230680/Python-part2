a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
n = a.count(5)
print("Результат работы программы: ")
print(f"Кол-во цифр <5> при первом объединении: {n} шт")
while n > 0:
    a.remove(5)
    n -= 1
a.extend(c)
n = a.count(3)
print(f"Кол-во цифр <3> во втором объединении: {n} шт")
print(f"Итоговый список: {a}")

# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)
#
# # TODO переписать программу
