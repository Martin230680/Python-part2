# TODO здесь писать код

# 1 вариант

old_cart_list = [3070, 2060, 3090, 3070, 3090]
new_list = []
maximum = old_cart_list[0]
for i in range(len(old_cart_list)):
    if old_cart_list[i] > maximum:
        maximum = old_cart_list[i]
for i in range(len(old_cart_list)):
    if old_cart_list[i] != maximum:
        new_list.append(old_cart_list[i])
print("Старый список видеокарт:", old_cart_list)
print("Новый список видеокарт:", new_list)

# 2 вариант

new_list1 = old_cart_list[:]
max_number = max(new_list1)
try:
    while True:
        new_list1.remove(max_number)
except ValueError:
    pass
print("Старый список видеокарт:", old_cart_list)
print("Новый список видеокарт:", new_list1)


# 3 вариант
new_list2 = [i for i in old_cart_list if i != max_number]
print("Старый список видеокарт:", old_cart_list)
print("Новый список видеокарт:", new_list2)
