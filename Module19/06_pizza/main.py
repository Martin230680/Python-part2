N = int(input("Введите количество заказов: "))
print("Введите заказы в формате: Заказчик Пицца Количество: ")
i = 0
order_dect = {}
temp_list = []
while i < N:
    order = input(f"{i+1}-й заказ: ")
    temp_list = order.split(" ")
    if temp_list[0] not in order_dect:
        order_dect[temp_list[0]] = {temp_list[1]: int(temp_list[2])}
    else:
        if temp_list[1] not in order_dect[temp_list[0]]:
            order_dect[temp_list[0]].update({temp_list[1]: int(temp_list[2])})
        else:
            order_dect[temp_list[0]][temp_list[1]] += int(temp_list[2])
    i += 1
key_list = sorted([ikey for ikey in order_dect])
for i_key in key_list:
    print(f"\033[31mКлиент:\033[0m {i_key.capitalize()}")
    key2_list = sorted([j_key for j_key in order_dect[i_key]])
    print("\033[34mЗаказ:\033[0m")
    for i_key2 in key2_list:
        print(f"{i_key2.capitalize()}: {order_dect[i_key][i_key2]} шт.")
print(order_dect)
