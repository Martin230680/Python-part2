nice_list = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
]
# 1 способ
nice_list = [y for x in nice_list for y in x]
nice_list = [y for x in nice_list for y in x]
print(nice_list)

# 2 способ
# def function2(i):
#     result.append(i)
#
#
# def function1(list):
#     list2 = [function2(i) for i in list]
#
#
# def function(list):
#     list1 = [function1(i) for i in list]
#
#
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#              [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# result = []
# result_list = [function(i) for i in nice_list]
# print(result)
