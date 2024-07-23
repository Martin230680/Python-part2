N = int(input("Кол-во человек: "))
members = list(range(1, N + 1))
steps = int(input("Какое число в считалке?: "))
print(f"Значит, выбывает каждый {steps}-й человек")

while N - 1 > 0:
    print("\nТекущий круг людей: ", members)
    begin_count = int(input("Начало счёта с номера: "))
    index_count = members.index(begin_count)
    index_out = steps % N - 1 + index_count
    print(f"Выбывает человек под номером: {members[index_out]}")
    members.remove(members[index_out])
    N -= 1
print(f"\nОстался человек под номером: {members[0]}")
# Кол-во человек: 5
# Какое число в считалке? 7
# Значит, выбывает каждый 7-й человек
#
# Текущий круг людей: [1, 2, 3, 4, 5]
# Начало счёта с номера 1
# Выбывает человек под номером 2
#
# Текущий круг людей: [1, 3, 4, 5]
# Начало счёта с номера 3
# Выбывает человек под номером 5
#
# Текущий круг людей: [1, 3, 4]
# Начало счёта с номера 1
# Выбывает человек под номером 1
#
# Текущий круг людей: [3, 4]
# Начало счёта с номера 3
# Выбывает человек под номером 3
#
# Остался человек под номером 4
