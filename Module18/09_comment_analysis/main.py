# TODO здесь писать код


def count_uppercase_lowercase(text_str):
    upper_case = 0
    lower_case = 0
    for symbol in text_str:
        if ("A" <= symbol <= "Z") or ("А" <= symbol <= "Я"):
            upper_case += 1
        elif ("a" <= symbol <= "z") or ("а" <= symbol <= "я"):
            lower_case += 1
    return upper_case, lower_case


text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print()
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
