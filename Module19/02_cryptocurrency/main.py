data = {
    "address": "0x544444444444",
    "ETH": {"balance": 444, "total_in": 444, "total_out": 4},
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False,
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0,
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False,
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0,
        },
    ],
}
keys_list = []
values_list = []
print("Словарь data:")
for index in data:
    print(f"Ключ: {index}", end=". ")
    print(f"Значение: {data.get(index)}")
    keys_list.append(index)
    values_list.append(data.get(index))
print("Список ключей: ", keys_list)
print("Список значений: ", values_list)
print()
print("Присвоение total_diff = 100")
data["ETH"]["total_diff"] = 100
print(data["ETH"])
print()
print('Замена на "doge')
data["tokens"][0]["fst_token_info"]["name"] = "doge"
temp_list = data["tokens"]
print(temp_list)
print()
print("Присвоение total_out = sum")
sum = 0
for index in temp_list:
    if "total_out" in index.keys():
        sum += index["total_out"]
data["ETH"]["total_out"] = sum
print(data["ETH"])
print()
print("Замена price на total_price")
temp_value = data["tokens"][1]["sec_token_info"].pop("price")
data["tokens"][1]["sec_token_info"]["total_price"] = temp_value
print(data["tokens"][1]["sec_token_info"])
