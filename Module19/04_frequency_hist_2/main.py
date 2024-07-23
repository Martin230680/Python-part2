text = input("Введите текст: ")
dect = {}
for i_char in text:
    if i_char in dect.keys():
        dect[i_char] += 1
    else:
        dect[i_char] = 1
print("Оригинальный словарь частот: ", dect)
max_val = max(dect.values())
new_dect = {}
dect_list = []
for i in range(max_val):
    for i_key, i_val in dect.items():
        if i_key not in dect_list and i_val == i + 1:
            dect_list.append(i_key)
            new_dect[i_val] = dect_list
    dect_list = []
print("Инвертированный словарь частот: ", new_dect)
