string = input("введите сроку: ")
temp_set = set()
for i_char in string:
    if i_char not in temp_set:
        temp_set.add(i_char)
    else:
        temp_set.remove(i_char)
if len(temp_set) > 1:
    print("нельзя сделать палиндромом.")
else:
    print("можно сделать палиндромом.")

# 2 способ

synonyms = dict()
pairs_count = int(input("Введите количество пар слов: "))

for i in range(pairs_count):
    first_word, second_word = input(f"{i + 1} пара: ").lower().split("-")
    synonyms[first_word] = second_word
    synonyms[second_word] = first_word

while True:
    word = input("Введите слово: ").lower()
    if word in synonyms:
        print("Синоним: ", synonyms[word])
        break
    else:
        print("Такого слова в словаре нет.")

