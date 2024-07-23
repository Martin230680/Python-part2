def summ(*args):
    num_list = [summ(*arg) if isinstance(arg, list) else arg for arg in args]
    return sum(num_list)


print(summ([[1, 2, [3]], [1], 3]))
print(summ(1, 2, 3, 4, 5))

# зачтено
