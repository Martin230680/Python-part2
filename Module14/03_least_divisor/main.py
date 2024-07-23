# TODO здесь писать код


def min_delitel(N):
    i = 1
    while i <= N:
        i += 1
        if N % i == 0:
            break
    return i


while True:
    N = int(input("Введите число N: "))
    if N <= 1:
        print("Число N должно быть больше 1, повторите ввод.")
    else:
        break

print(f"Наименьший делитль числа {N}, является число {min_delitel(N)}")
