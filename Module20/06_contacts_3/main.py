def fio(fi):
    return fi[0].capitalize(), fi[1].capitalize()


dect1 = {}
while True:
    while True:
        print("Введите номер действия:")
        print("1. Добавить контакт.")
        print("2. Поиск человека.")
        case = input("1 / 2 ? : ")
        print(case)
        if "1" < case < "2":
            print("Неверный выбор, повторите ввод.")
        else:
            break
    if case == "1":
        fi = (
            input("Введите имя и фамилию нового контакта (через пробел): ")
            .lower()
            .split()
        )
        tel = input("Введите номер телефона: ")
        fio1 = fio(fi)
        if fio1 not in dect1:
            dect1[fio1] = tel
        else:
            print("Такой человек уже есть в контактах.")
        print("Текущий словарь контактов: ", dect1)
    else:
        fio_search = input("Введите фамилию для поиска: ")
        for i_key in dect1:
            if i_key[0].lower() == fio_search.lower():
                print(i_key[0], i_key[1], dect1[i_key])
