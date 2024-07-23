goods = {
    "Лампа": "12345",
    "Стол": "23456",
    "Диван": "34567",
    "Стул": "45678",
}

store = {
    "12345": [
        {"quantity": 27, "price": 42},
    ],
    "23456": [
        {"quantity": 22, "price": 510},
        {"quantity": 32, "price": 520},
    ],
    "34567": [
        {"quantity": 2, "price": 1200},
        {"quantity": 1, "price": 1150},
    ],
    "45678": [
        {"quantity": 50, "price": 100},
        {"quantity": 12, "price": 95},
        {"quantity": 43, "price": 97},
    ],
}

for goods_k, goods_v in goods.items():
    print(goods_k + " - ", end=" ")
    sum = 0
    count = 0
    for member_k in store[goods_v]:
        sum += member_k["quantity"] * member_k["price"]
        count += member_k["quantity"]
    print(f"На скаладе {count} шт., стимость {sum} руб.")
