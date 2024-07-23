def fun_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    reference_elem = num_list[-1]
    left_list = []
    midl_list = []
    right_list = []
    for i_elem in num_list:
        if i_elem < reference_elem:
            left_list.append(i_elem)
        elif i_elem == reference_elem:
            midl_list.append(i_elem)
        else:
            right_list.append(i_elem)
    return fun_sort(left_list) + midl_list + fun_sort(right_list)


num_list = [5, 8, 9, 4, 2, 9, 1, 8, -2, 0, -10]

print(fun_sort(num_list))

# зачтено
