# TODO здесь писать

def decorator(func):

    def wrapped_func(*args, **kwargs):
        if args in wrapped_func.cache:
            return wrapped_func.cache[args]
        else:
            result = func(*args, **kwargs)
            wrapped_func.cache[args] = result
            print(f'В КЭШ запишем значение функции от {args[0]} - {wrapped_func.cache[args]}')
            return result
    wrapped_func.cache = {}
    return wrapped_func


@decorator
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(8))
print(fibonacci(15))