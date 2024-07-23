students = {
    1: {
        "name": "Bob",
        "surname": "Vazovski",
        "age": 23,
        "interests": ["biology, swimming"],
    },
    2: {
        "name": "Rob",
        "surname": "Stepanov",
        "age": 24,
        "interests": ["math", "computer games", "running"],
    },
    3: {
        "name": "Alexander",
        "surname": "Krug",
        "age": 22,
        "interests": ["languages", "health food"],
    },
}


def count_interests(dect1):
    count_surname = 0
    interests_list = []
    for i_key in dect1:
        count_surname += len(students[i_key]["surname"])
        interests_list += students[i_key]["interests"]
    return count_surname, interests_list


pears = [(i_key, students[i_key]["age"]) for i_key in students]
print("\033[31mСписок пар (ID студента - возраст): \033[0m", pears)
count_surname, interests_list = count_interests(students)
print("\033[31mКоличество букв в именах словаря: \033[0m", count_surname)
print("\033[31mСписок интересов у студентов: \033[0m", interests_list)


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
# print(pairs)
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)
