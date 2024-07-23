# TODO здесь писать код
# 1 способ
# text = input('Введите строку: ')
# text_list = text.split()
# new_list = []
# for word in text_list:
#     new_list.append(word.capitalize())
# new_text = ' '.join(new_list)
# print('Результат:', new_text)

# 2 способ

text = input("Введите строку: ")
new_txt = text.title()
print("Результат:", new_txt)
