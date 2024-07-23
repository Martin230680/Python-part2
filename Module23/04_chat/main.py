import os

while True:
    try:
        user_name = input("Введите ваше имя, допускаются только буквы и цифры: ")
        for i_name in user_name:
            if not i_name.isalpha() and not i_name.isdigit():
                raise ValueError
        break
    except ValueError:
        print("Неправильный ввод! Повторите ввод.\n")

while True:
    print("Какое действие хотите осуществить?")
    print("1. Посмотреть историю чата.")
    print("2. Отправить сообщение.")
    print("3. Выйти из чата.")
    num = int(input("\nВыбирите номер действия: "))
    if num == 1:
        try:
            if not os.path.exists("history.txt") or os.stat("history.txt").st_size == 0:
                raise FileNotFoundError
            else:
                with open("history.txt", "r", encoding="utf-8") as file_chat:
                    print(f"Текст чата: \n\n{file_chat.read()}")
        except FileNotFoundError:
            print("Нет истории чата. Чат пустой.")
    elif num == 2:
        try:
            with open("history.txt", "a", encoding="utf-8") as msg:
                message = input(f"\n{user_name.capitalize()}: Введите Ваше сообщение:\n")
                if len(message) == 0:
                    raise ValueError
                else:
                    msg.write(f"{user_name}: {message}\n")
        except ValueError:
            print("Вы не ввели ни одного слова. Сообщение Пустое.")
    elif num == 3:
        break
    else:
        print("Ошибка! Неверный номер действия.")

# зачтено
