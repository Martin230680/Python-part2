def input_weight_cont(num_cont):
    set_weight = []
    num_cont1 = num_cont
    while num_cont > 0:
        while True:
            cont_weight = int(
                input(f"Введите вес {num_cont1 - (num_cont - 1)} - го контейнера: ")
            )
            if cont_weight <= 200:
                set_weight.append(cont_weight)
                num_cont -= 1
                break
            else:
                print("Вес контейнера более 200кг, введите заово вес:")
    return set_weight


def put_new_cont(set_weight):
    while True:
        new_cont = int(input("Введите вес нового контейнера: "))
        if new_cont > 200:
            print("Вес контейнера более 200кг, введите заово вес:")
        else:
            break
    count = 0
    for i in set_weight:
        count += 1
        if i >= new_cont:
            continue
        else:
            break
    return count


num_cont = int(input("Введите количество контейнеров: "))
set_weight = input_weight_cont(num_cont)
count = put_new_cont(set_weight)
print(f"Номер, который получит новый контейнер: {count}")
