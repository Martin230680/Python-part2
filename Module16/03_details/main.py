shop = [
    ["каретка", 1200],
    ["шатун", 1000],
    ["седло", 300],
    ["педаль", 100],
    ["седло", 1500],
    ["рама", 12000],
    ["обод", 2000],
    ["шатун", 200],
    ["седло", 2700],
]

N = len(shop)
count_detail = 0
sum_detail = 0
name_detail = input("Название детали: ")
for i_name in range(N):
    if shop[i_name][0] == name_detail:
        count_detail += 1
        sum_detail += shop[i_name][1]
print(f"Кол-во деталей: {count_detail}")
print(f"Общая стоимость: {sum_detail}")
