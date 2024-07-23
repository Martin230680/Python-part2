new_file = open("first_tour.txt", "r")
count_tour1 = int(new_file.readline())
tmp_list = []
for line in new_file:
    new_line = line.split()
    if new_line != [] and int(new_line[-1]) > count_tour1:
        tmp_list.append(new_line)
new_file.close()
tmp_list.sort(key=lambda i: int(i[-1]))
tmp_list.reverse()
count_tour2 = str(len(tmp_list)) + "\n"
n = 1
second_file = open("second_tour.txt", "w")
second_file.write(count_tour2)
for i in tmp_list:
    line_file = str(n) + ") " + i[-2][0] + ". " + i[0] + " " + i[-1] + "\n"
    print(f"{n}) {i[-2][0]}. {i[0]} {i[-1]}")
    n += 1
    second_file.write(line_file)
second_file.close()

# зачтено
