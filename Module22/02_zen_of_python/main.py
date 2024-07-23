my_file = open("zen.txt", "r")
my_list = list(my_file)
for i in range(1, len(my_list)):
    if "\n" in my_list[-i]:
        print(my_list[-i], end="")
    else:
        print(my_list[-i])

print("****************************")
my_file = open("zen.txt", "a")
my_file.write("\n")
my_file.close()
my_file = open("zen.txt", "r")
my_list = list(my_file)
my_list.reverse()
for i in my_list:
    print("".join(i), end="")
my_file.close()
print("****************************")

# зачтено
