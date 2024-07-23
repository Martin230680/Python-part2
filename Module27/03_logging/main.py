from typing import Callable, Any
import datetime


def logging(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            dt = datetime.datetime.now().strftime('%m.%d.%Y %H:%M:%S')
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write(f'[{dt}] - {func.__name__}: ERROR: [{e}]\n')

    return wrapped_func


@logging
def func1() -> int:
    print('Функция 1: Чтобы не было ошибок введите целое число.')
    number_int = int(input('Введите число: '))
    return number_int


@logging
def func2() -> int:
    print('Функция 2: Чтобы не было ошибок введите целое число.')
    number_int = int(input('Введите число: '))
    return number_int

@logging
def func3() -> int:
    print('Функция 3: Чтобы не было ошибок введите целое число.')
    number_int = int(input('Введите число: '))
    return number_int



func1()
func2()
func3()