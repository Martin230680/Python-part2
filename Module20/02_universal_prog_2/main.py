set1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)
dect1 = {
    "Alex": 27,
    "Vova": 35,
    "Bob": 45,
    "Karl": 34,
    "Sem": 55,
    "Marry": 18,
    "Dasha": 20,
}
str1 = "В строке ищем буквы у которых индекс простое число"
list1 = [
    ["каретка", 1200],
    ["шатун", 1000],
    ["седло", 300],
    ["педаль", 100],
    ["седло", 1500],
    ["рама", 12000],
    ["обод", 2000],
    ["шатун", 200],
    ["седло", 2700],
]


def is_prime(index):
    flag = 0
    for i in range(2, index // +1):
        if index % i == 0:
            flag = 1
            break
    return flag


def experimentalist(iter_object):
    result_list = []
    for i_index, i_val in enumerate(iter_object):
        if i_index > 1:
            if is_prime(i_index) == 0:
                result_list.append(i_val)
    return result_list


print(experimentalist(set1))
print(experimentalist(dect1))
print(experimentalist(str1))
print(experimentalist(list1))
