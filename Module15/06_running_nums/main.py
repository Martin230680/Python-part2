old_list = [1, 2, 3, 4, 5]
step = int(input("Ввеедите шаг сдвига: "))
new_list = []
difference = step * (-1)

while step != 0:
    for _ in range(step):
        new_list.append(old_list[-step])
        step -= 1

for i in old_list[:difference]:
    new_list.append(i)

print(
    f"""Начальный список: {old_list}
Сдвинутый список: {new_list}"""
)
