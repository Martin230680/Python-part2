errors_list = []
with open("people.txt", "r", encoding="utf-8") as people_file:
    name_line = people_file.read().split("\n")
    print(name_line)
    res = "".join(name_line)
    try:
        for number, name in enumerate(name_line):
            if len(name) < 3:
                errors_list.append(number + 1)
        if errors_list:
            raise Exception("менее трёх символов в строкaх", errors_list)
    finally:
        print(f"Общее количество символов: {len(res)}")

# зачтено
