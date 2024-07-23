dict1 = {}
count_char = 0
my_file = open("text_5.txt", "r")
for i_line in my_file:
    for char in i_line:
        if char.isalpha():
            if char in dict1.keys():
                dict1[char.lower()] += 1
                count_char += 1
            else:
                dict1[char.lower()] = 1
                count_char += 1
my_file.close()
temp_list = [[i_key, round(i_val / count_char, 3)] for i_key, i_val in dict1.items()]
temp_list.sort(key=lambda i: (i[-1], i[0]))
print(temp_list)
my_file2 = open("analysis.txt", "w")
for i in temp_list:
    str_file = i[0] + " " + str(i[1]) + "\n"
    my_file2.write(str_file)
my_file2.close()

# зачтено
