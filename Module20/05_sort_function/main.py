def sort_function(tpl):
    list1 = [tpl[i] for i in range(len(tpl))]
    if sum(list1) % 1 != 0:
        return tpl
    else:
        for i in range(len(tpl) - 1):
            for j in range(len(tpl) - i - 1):
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
        tpl_sorted = tuple(list1)
        return tpl_sorted


tpl1 = (-5, 6, 0, 33, 10, 4, 3, -11, -1, 100)
tpl11 = (-5, 6, 0, 33, 10, 4.5, 3, -11, -1, 100)
print(tpl1)
tpl2 = sort_function(tpl1)
print(tpl2)
print()
print(tpl11)
tpl2 = sort_function(tpl11)
print(tpl2)
