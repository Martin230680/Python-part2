import random


def random_1_of_13():
    result = True
    number = random.randint(1, 13)
    if number == 1:
        result = False
    return result


def write_in_file(number, flag=0):
    if flag == 0:
        my_file = open("out_file.txt", "w")
        my_file.write(str(number) + "\n")
        my_file.close()
    else:
        with open("out_file.txt", "a", encoding="utf8") as my_file:
            my_file.write(str(number) + "\n")
    return


summ = 0
flag_record = 0
while summ <= 777:
    num = int(input("Введите число: "))
    if flag_record == 0:
        write_in_file(num)
        flag_record = 1
    else:
        if random_1_of_13():
            write_in_file(num, 1)
        else:
            try:
                ex = random.randint(1, 3)
                if ex == 1:
                    raise AttributeError("Ошибка атрибута")
                elif ex == 2:
                    raise EOFError("Ошибка чтения из файла")
                else:
                    raise TypeError("Ощибка типа")
            except Exception as e:
                print(e)
            break
    summ += num
else:
    print("Сумма чисел превышает max - 777!")

# зачтено
