def input_size_skates(N):
    list_size_skates = []
    for i in range(N):
        size_skates = int(input(f"Размер {i + 1}-й пары: "))
        list_size_skates.append(size_skates)
    return list_size_skates


def input_size_legs(N):
    list_size_legs = []
    for i in range(N):
        size_leg = int(input(f"Размер ноги {i + 1}-го человека: "))
        list_size_legs.append(size_leg)
    return list_size_legs


kol_skates = int(input("Введите кол-во коньков: "))
list_size_skates = input_size_skates(kol_skates)
kol_people = int(input("\nВведите кол-во людей: "))
list_size_legs = input_size_legs(kol_people)
count_pears = 0
for i in range(kol_people):
    if list_size_legs[i] in list_size_skates:
        list_size_skates.remove(list_size_legs[i])
        count_pears += 1
print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {count_pears}")
# Кол-во коньков: 4
# Размер 1-й пары: 41
# Размер 2-й пары: 40
# Размер 3-й пары: 39
# Размер 4-й пары: 42
#
# Кол-во людей: 3
# Размер ноги 1-го человека: 42
# Размер ноги 2-го человека: 41
# Размер ноги 3-го человека: 42
