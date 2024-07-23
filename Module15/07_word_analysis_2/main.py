import math

word = input("Введите слово для проверки: ")
len_word = len(word)
word_list = list(word)
flag_polin = 0
halh_word_ceil = math.ceil(len_word / 2)
for i in range(1, halh_word_ceil + 1):
    if word_list[i - 1].lower() == word_list[-i].lower():
        flag_polin += 1
if flag_polin == halh_word_ceil:
    print(f'Слово "{word}" - является палиндромом')
else:
    print(f'Слово "{word}" - НЕ является палиндромом')
