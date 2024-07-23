def merge_sorted_lists(list1, list2):
    list1.extend(list2)
    print(f"Объединенный список: {list1}")
    N = len(list1)
    a = 1
    while a < N:
        min = list1[a - 1]
        for i in range(a, N):
            if list1[i] == min:
                N = N - 1
                list1.remove(list1[i])
                a -= 1
                break
            elif list1[i] < min:
                min = list1[i]
                list1[i] = list1[a - 1]
                list1[a - 1] = min
        a += 1
    return list1


list1 = [1, 3, 5, 7, 9, 8, 10, 5, -3, -2, 11, 12]
print(f"Исходный первый список: {list1}")
list2 = [2, 4, 5, 6, 8, 10, 10, 10, 0, -3, 11, 12]
print(f"Исходный второй список: {list2}")
merged = merge_sorted_lists(list1, list2)
print(f"упорядоченный объединенный список без лишних элементов: {merged}")
