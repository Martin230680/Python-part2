nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]


def num_list(tmp_list, result_list=None):
    if result_list is None:
        result_list = []
    for i_elem in tmp_list:
        if isinstance(i_elem, int):
            result_list.append(i_elem)
        if isinstance(i_elem, list):
            # Надо не забыть здесь расширить наш список рекурсивными вызовами, которые потом вычисляться
            result_list.extend(num_list(i_elem))

    return result_list


print(num_list(nice_list))

# зачтено
