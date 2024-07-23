num_list = [1, 3, -9, 0, -10, 2]
N = len(num_list)
a = 1
while a < N:
    min = num_list[a - 1]
    for i in range(a, N):
        if num_list[i] < min:
            min = num_list[i]
            num_list[i] = num_list[a - 1]
            num_list[a - 1] = min
    a += 1
print(num_list)
