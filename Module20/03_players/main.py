players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2),
}

# TODO здесь писать код
temp_list1 = []
temp_list2 = []
result = []
for i_key, j_val in players.items():
    temp_list1.append(i_key)
    temp_list2.append(j_val)
for index in range(len(players)):
    result.append(temp_list1[index] + temp_list2[index])
print(result)

print([i_key + i_val for i_key, i_val in players.items()])
