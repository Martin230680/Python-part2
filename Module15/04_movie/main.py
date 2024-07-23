def lower_list(films_list):
    films1 = films_list[:]
    for i in range(len(films1) - 1):
        films1[i] = films1[i].lower()
    return films1


def bests_films(N, films1):
    best_list = []
    while N > 0:
        film = input("Введите название фильма: ")
        if film in films1:
            if film in best_list:
                print("Ошибка: Вы уже выбрали этот фильм")
            else:
                best_list.append(film)
                N -= 1
        else:
            print(f'Ошибка: фильма - "{film}" у нас нет :(')
    return best_list


films_list = [
    "Крепкий орешек",
    "Назад в будущее",
    "Таксист",
    "Леон",
    "Богемская рапсодия",
    "Город грехов",
    "Мементо",
    "Отступники",
    "Деревня",
]
films1 = lower_list(films_list)
N = int(input("Сколько фильмов хотите добавить: "))
best_list = bests_films(N, films1)
best_list = [best.capitalize() for best in best_list]
print("Ваш список любимых фильмов:", best_list)
