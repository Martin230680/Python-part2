# TODO здесь писать код

# 1 способ

# str1 = input('Введите 1-ю строку: ')
# str2 = input('Введите 2-ю строку: ')
# while len(str1) != len(str2):
#     str2 = input('Введите 2-ю строку повторно, не соответствует длине 1-ой строки: ')
# if not str1 == str2:
#     count = 0
#     str_list = list(str1)
#     count_for = len(str1)
#     while count_for > 0:
#         last_char = str_list[-1:]
#         begin_str = str_list[:-1]
#         new_list = [j for i in [last_char, begin_str] for j in i]
#         count += 1
#         new_str = ''.join(new_list)
#         if new_str == str2:
#             print('Первая строка получается из второй со сдвигом {delta}.'.format(delta=count))
#             break
#         else:
#             str_list = new_list
#             count_for -= 1
#     else:
#         print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
# else:
#     print('Строки одинаковые с самого начала, проверка не нужна')


# 2 способ

str1 = input("Введите 1-ю строку: ")
str2 = input("Введите 2-ю строку: ")
new_str = ""
while len(str1) != len(str2):
    str2 = input("Введите 2-ю строку повторно, не соответствует длине 1-ой строки: ")
if not str1 == str2:
    new_str = str1 * 2
    index = new_str.find(str2)
    if index == -1:
        print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
    else:
        delta = len(str1) - index
        print(
            "Первая строка получается из второй со сдвигом {delta}.".format(delta=delta)
        )
else:
    print("Строки одинаковые с самого начала, проверка не нужна")
