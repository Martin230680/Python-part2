def validation(check_list, count):
    file_line = " ".join(check_list)
    try:
        if len(check_list) != 3:
            raise IndexError
        if not check_list[0].isalpha():
            raise NameError
        if check_list[1].count("@") == 0 or check_list[1].count(".") == 0:
            raise SyntaxError
        if check_list[2].isdigit():
            if int(check_list[2]) < 10 or int(check_list[2]) > 99:
                raise ValueError
    except IndexError:
        file_bad.write(f"Строка {count}: {file_line} НЕ присутствуют все три поля\n")
    except NameError:
        file_bad.write(f"Строка {count}: {file_line} Поле «Имя» содержит НЕ только буквы\n")
    except SyntaxError:
        file_bad.write(f"Строка {count}: {file_line} Поле «Имейл» НЕ содержит @ или точку\n")
    except ValueError:
        file_bad.write(f"Строка {count}: {file_line} Поле «Возраст» НЕ представляет число от 10 до 99\n")

    else:
        file_ok.write(f"Строка {count}: {file_line} - Ok\n")


with open("registrations.txt", "r", encoding="utf-8") as file_reg, open(
    "registrations_good.log", "w", encoding="utf-8"
) as file_ok, open("registrations_bad.log", "w", encoding="utf-8") as file_bad:
    count = 0
    for i_fileline in file_reg:
        guest_item = i_fileline.split()
        count += 1
        validation(guest_item, count)

# зачтено
