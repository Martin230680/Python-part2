# TODO здесь писать код
def list_odd_numbers(N):
    list_odd = []
    for i in range(N):
        if (i + 1) % 2 != 0:
            list_odd.append(i + 1)
    return list_odd


N = int(input("Input number: N = "))
print("Список нечетных чисел: ", list_odd_numbers(N))
