# TODO здесь писать код
text = input("Введите строку слов, разделяя их пробелом: ")
text_list = text.split()
print(text_list)
max = 0
flag = 0
for i in range(len(text_list)):
    if (len(text_list[i])) > max:
        max = len(text_list[i])
        flag = i
print('Самое длинное слово, первое по списку: "{word}"'.format(word=text_list[flag]))
print("Длина этого слова: {number} симво(л/ов).".format(number=max))
