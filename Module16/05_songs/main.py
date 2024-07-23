violator_songs = [
    ["World in My Eyes", 4.86],
    ["Sweetest Perfection", 4.43],
    ["Personal Jesus", 4.56],
    ["Halo", 4.9],
    ["Waiting for the Night", 6.07],
    ["Enjoy the Silence", 4.20],
    ["Policy of Truth", 4.76],
    ["Blue Dress", 4.29],
    ["Clean", 5.83],
]

N = int(input("Сколько песен выбрать? "))
total_time = 0
for i_playlist in range(N):
    song = input(f"Название {i_playlist + 1}-й песни: ")
    for i_song in range(len(violator_songs)):
        if violator_songs[i_song][0] == song:
            total_time += violator_songs[i_song][1]

print(f"\nбщее время звучания песен: {round(total_time, 2)} минуты")

# Сколько песен выбрать? 3
# Название 1-й песни: Halo
# Название 2-й песни: Enjoy the Silence
# Название 3-й песни: Clean
#
# Общее время звучания песен: 14.93 минуты
