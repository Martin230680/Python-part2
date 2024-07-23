# TODO здесь писать код
def fun_sum(N):
    i = N
    summ = 0
    while i != 0:
        summ = summ + i % 10
        i = int(i / 10)
    return summ


def count_num(N):
    count = 0
    while N != 0:
        count += 1
        N = N // 10
    return count


def sum_dif(summ, count):
    result = summ - count
    return result


N = int(input("Input N: "))
summ = fun_sum(N)
count = count_num(N)
result = sum_dif(summ, count)
print(
    f"Сумма цифр в числе {N}: {summ}, количество цифор в числе {N}: {count}. Разность суммы и количества: {result} "
)
