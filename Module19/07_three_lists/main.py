array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
array1_set = set(array_1)
array2_set = set(array_2)
array3_set = set(array_3)

print("\033[31mРешение с применением множеств:\033[0m")
print("Элементы, которые есть в каждом списке:")
print(sorted(array1_set & array2_set & array3_set))
print("Элементы из первого списка, которых нет во втором и третьем списках:")
print(sorted(array1_set - array2_set - array3_set))
print()
print("\033[31mРешение без применения множеств:\033[0m")
new_list = []
new_list1 = []
for i in array_1:
    if i in array_2 and i in array_3:
        new_list.append(i)
print("Элементы, которые есть в каждом списке:")
print(sorted(new_list))

for i in array_1:
    if i not in array_2 and i not in array_3:
        new_list1.append(i)
print("Элементы из первого списка, которых нет во втором и третьем списках:")
print(sorted(new_list1))
