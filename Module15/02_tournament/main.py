# TODO здесь писать код
first_day_list = []
name_list = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
print("Список укастников: - ", name_list)
for i in range(1, len(name_list) + 1, 1):
    if i % 2 != 0:
        first_day_list.append(name_list[i - 1])
print("Участники первого дня: - ", first_day_list)
