# 1 способ
def codding(i, language):
    index = language.index(i)
    new_index = index + offset
    code = language[new_index]
    return code


def list_to_text(list):
    code_st = ""
    for i in list:
        code_st += i
    return code_st


alphabet_rus = [
    "А",
    "Б",
    "В",
    "Г",
    "Д",
    "Е",
    "Ё",
    "Ж",
    "З",
    "И",
    "Й",
    "К",
    "Л",
    "М",
    "Н",
    "О",
    "П",
    "Р",
    "С",
    "Т",
    "У",
    "Ф",
    "Х",
    "Ц",
    "Ч",
    "Ш",
    "Щ",
    "Ъ",
    "Ы",
    "Ь",
    "Э",
    "Ю",
    "Я",
    "А",
    "Б",
    "В",
    "Г",
    "Д",
    "Е",
    "Ё",
    "Ж",
    "З",
    "И",
    "Й",
    "К",
    "Л",
    "М",
    "Н",
    "О",
    "П",
    "Р",
    "С",
    "Т",
    "У",
    "Ф",
    "Х",
    "Ц",
    "Ч",
    "Ш",
    "Щ",
    "Ъ",
    "Ы",
    "Ь",
    "Э",
    "Ю",
    "Я",
]
alphabet_eng = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

offset = int(input("Введите шаг шифровки: "))
text = input("Введите сообщение для шифровки: ").upper()
lang = int(input('Выберите язык текста "1" -(русский) "2" -(английский): '))
if lang == 1:
    language = alphabet_rus
else:
    language = alphabet_eng
code = [(codding(i, language)).lower() if i in language else i.lower() for i in text]
code_st = list_to_text(code)
print(code_st)


# 2 способ


def codding2(language, text, offset):
    code = ""
    for i in text:
        index = language.find(i)
        new_index = index + offset
        if i in language:
            code += language[new_index]
        else:
            code += i
    return code


alphabet_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
offset = int(input("Введите шаг шифровки: "))
text = input("Введите сообщение для шифровки: ").upper()
lang = int(input('Выберите язык текста "1" -(русский) "2" -(английский): '))
if lang == 1:
    language = alphabet_rus
else:
    language = alphabet_eng
code = codding2(language, text, offset)
print(code.lower())
