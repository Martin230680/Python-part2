# TODO здесь писать код
def count_num(N, N_const):
    if N == 0:
        return
    print(N_const - N + 1)
    count_num(N - 1, N_const)


N = int(input("Введите количество циклов: "))
count_num(N, N)

# зачтено
