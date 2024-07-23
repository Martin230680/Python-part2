# TODO здесь писать код
error_list = ["@", "№", "$", "%", "^", "&", "*", "(", ")"]
name_file = input("Введите название файла: ")
if not name_file.endswith(".txt") and not name_file.endswith(".docx"):
    print("Неверное расширение файла. Ожидалось .txt или .docx.")
elif name_file[:1] in error_list:
    print(
        "Ошибка: название начинается недопустимым символом: - {error}".format(
            error=name_file[:1]
        )
    )
else:
    print("Файл назван верно.")
