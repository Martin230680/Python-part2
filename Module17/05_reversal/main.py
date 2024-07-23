text = input("Введите строку: ")
list_h = [i for i in range(len(text)) if text[i] == "h"]
print(
    "Развёрнутая последовательность между первым и последним h:",
    text[list_h[-1] - 1 : list_h[0] : -1],
)
