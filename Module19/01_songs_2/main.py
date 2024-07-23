violator_songs = {
    "World in My Eyes": 4.86,
    "Sweetest Perfection": 4.43,
    "Personal Jesus": 4.56,
    "Halo": 4.9,
    "Waiting for the Night": 6.07,
    "Enjoy the Silence": 4.20,
    "Policy of Truth": 4.76,
    "Blue Dress": 4.29,
    "Clean": 5.83,
}
# 1 способ
N = int(input("Введите количество песен: "))
i = 0
total = 0
trek_list = []
while i < N:
    while True:
        song = input(f"Введите название {i + 1} - ой песни: ")
        if song in violator_songs.keys():
            if song not in trek_list:
                trek_list.append(song)
                total += violator_songs[song]
                i += 1
                break
            else:
                print("Песня с этим названием уже выбрана, повторите ввод.")
        else:
            print("Песни нет в списке, повторите ввод.")
trekstr = " ".join(trek_list)
print("Выбранный треклист: ", trekstr)
print("Общая продолжительность: ", round(total, 2))

# 2 способ
N = int(input("Введите количество песен: "))
i = 0
total = 0
trek_list = set()
while i < N:
    while True:
        song = input(f"Введите название {i + 1} - ой песни: ")
        if song in violator_songs:
            if song not in trek_list:
                trek_list.add(song)
                total += violator_songs.get(song)
                i += 1
                break
            else:
                print("Песня с этим названием уже выбрана, повторите ввод.")
        else:
            print("Песни нет в списке, повторите ввод.")
trek_str = " ,".join(trek_list)
print("Выбранный треклист: ", trek_str)
print("Общая продолжительность: ", round(total, 2))

# 3 способ с использованием get и значения по умолчанию.

# N = int(input('Введите количество песен: '))
# i = 0
# total = 0
# trek_list = set()
# while i < N:
#     key = input(f'Введите название {i + 1} - ой песни: ')
#     song = violator_songs.get(key, 0)
#     total += song
#     i += 1
# print('Общая продолжительность: ', round(total,2))
