import zipfile

zip_file = zipfile.ZipFile("voyna-i-mir.zip", "r")
zip_file.extractall("./")

dict1 = {}
my_file = open("voyna-i-mir.txt", "r", encoding="utf-8")
for i_line in my_file:
    for char in i_line:
        if char.isalpha():
            if char in dict1.keys():
                dict1[char] += 1
            else:
                dict1[char] = 1
my_file.close()
temp_list = [[i_key, i_val] for i_key, i_val in dict1.items()]
temp_list.sort(key=lambda i: (i[-1], i[0]))
for i in temp_list:
    str_file = str(i[0]) + " " + str(i[1])
    print(str_file)

# зачтено
