my_file = open("numbers.txt", "r")
sum = 0
for i_line in my_file:
    for char in i_line:
        if "0" <= char <= "9":
            sum += int(char)
my_file.close()
sum_file = open("answer.txt", "w")
sum_file.write(str(sum))
sum_file.close()

# зачтено
