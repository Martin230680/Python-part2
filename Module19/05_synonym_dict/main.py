pear = int(input("Введите количество пар слов: "))
dect1 = {}
temp_list = []
text_temp = ""
flag = 0
for i in range(pear):
    text = input(f"Введите {i + 1}-ю пару синонимов через дефис: ")
    text_temp = text.replace(" ", "").lower()
    temp_list = text_temp.split("-")
    dect1[temp_list[0]] = temp_list[1]
while True:
    word = input("Введите слово: ").lower()
    for i_key, j_val in dect1.items():
        if word == i_key:
            print("Синоним: ", j_val.capitalize())
            break
        elif word == j_val:
            print("Синоним: ", i_key.capitalize())
            break
        else:
            flag += 1
    if flag == pear:
        print("Такого слова в словаре нет.")
    else:
        break
