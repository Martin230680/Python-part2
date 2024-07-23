# TODO здесь писать код
print('Генератор пароля. Чтобы выйти из режима нажмите "q" или "Q"')
while True:
    password = input("Введите пароль:")
    if password == "q" or password == "Q":
        break
    else:
        if not len(password) < 8:
            count_num = 0
            count_letter = 0
            for simbol in password:
                if "0" <= simbol <= "9":
                    count_num += 1
                elif "A" <= simbol <= "Z":
                    count_letter += 1
            if count_num >= 3 and count_letter >= 1:
                print("Пароль надежный!")
            else:
                print("Пароль ненадежный. Попробуйте еще раз.")
        else:
            print("Пароль менее 8 символов, повторите ввод.")
