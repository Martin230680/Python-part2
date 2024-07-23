import random


class Students:
    def __init__(self, fio, group_num, academic_per):
        self.fio = fio
        self.group_num = group_num
        self.academic_performance = academic_per

    def average(self):
        return sum(self.academic_performance) / len(self.academic_performance)

    def students_info(self):
        print(self.fio, self.group_num, self.average())


studets_list = [['Иванов Иван', 2201, [random.randint(1, 5) for _ in range(5)]],
                ['Петров Петр', 2202, [random.randint(3, 5) for _ in range(5)]],
                ['Сидоров Иван', 2201, [random.randint(2, 5) for _ in range(5)]],
                ['Кузнецов Андрей', 2202, [random.randint(4, 5) for _ in range(5)]],
                ['Андреев Кирилл', 2201, [random.randint(2, 5) for _ in range(5)]],
                ['Костин Коля', 2203, [random.randint(3, 5) for _ in range(5)]],
                ['Самойлов Иван', 2205, [random.randint(4, 5) for _ in range(5)]],
                ['Овечкин Александр', 2201, [random.randint(3, 5) for _ in range(5)]],
                ['Карпин Андрей', 2203, [random.randint(2, 5) for _ in range(5)]],
                ['Фетисов Слава', 2201, [random.randint(1, 5) for _ in range(5)]]]

students_objects = []
for i in range(len(studets_list)):
    students_objects.append(Students(studets_list[i][0], studets_list[i][1], studets_list[i][2]))

sort_students = sorted(students_objects, key=lambda item: item.average())

for student in sort_students:
    student.students_info()