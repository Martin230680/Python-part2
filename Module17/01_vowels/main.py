char_list = [
    "а",
    "у",
    "о",
    "ы",
    "и",
    "э",
    "я",
    "ю",
    "ё",
    "е",
    "А",
    "У",
    "О",
    "Ы",
    "И",
    "Э",
    "Я",
    "Ю",
    "Ё",
    "Е",
]
full_str = input("Введите строку: ")
result_list = [full_str[i] for i in range(len(full_str)) if full_str[i] in char_list]
print(result_list)
print(f"В тексте {len(result_list)} глас. букв.")
