# TODO здесь писать код
def proverka(member):
    num_flag = 0
    code_error = 0
    for index in member:
        if index >= "0" and index <= "9":
            num_flag += 1
    if num_flag == len(member):
        if int(member) < 0 or int(member) > 255:
            code_error = 2
            return code_error
        return code_error
    else:
        code_error = 1
        return code_error


print('Генератор пароля. Чтобы выйти из режима нажмите "q" или "Q"')
while True:
    flag1 = 0
    ok = 0
    ip = input("Введите IP адрес:")
    if ip == "q" or ip == "Q":
        break
    else:
        if not ip[-1] == ".":
            ip_list = ip.split(".")
            if len(ip_list) != 4:
                print(
                    "Ошибка: ip-адрес должен состоять из 4 чисел, разделенные точками. Повторите ввод."
                )
            else:
                for i_list in ip_list:
                    code = proverka(i_list)
                    if code == 2:
                        print(
                            'Ошибка: число "{num}" не в диапазоне (0-255)'.format(
                                num=i_list
                            )
                        )
                    elif code == 1:
                        print(
                            'Ошибка: число "{num}" не является целым числом'.format(
                                num=i_list
                            )
                        )
                    else:
                        ok += 1
                if ok == 4:
                    print("IP-адрес корректен.")
                else:
                    print("IP-адрес содержит ошибки, попробуйте снова.")
        else:
            print('Ошибка: ip-адрес не должен заканчиваться "."!')
