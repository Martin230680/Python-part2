# TODO здесь писать код
text = input("Введите строку: ")
count_symbol = 1
new_list = []
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count_symbol += 1
    else:
        new_list.append(text[i])
        new_list.append(str(count_symbol))
        count_symbol = 1
new_list.append(text[len(text) - 1])
new_list.append(str(count_symbol))
new_text = "".join(new_list)
print(new_text)
