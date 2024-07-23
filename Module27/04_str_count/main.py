from typing import Callable, Any


def count(func: Callable) -> Callable:
    print('Вызывается декоратор')

    def wrapped_func(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        wrapped_func.count += 1
        return result

    wrapped_func.count = 0
    return wrapped_func


@count
def func() -> None:
    print('<Тут что-то происходит...>')


@count
def func2() -> None:
    print('<Тут что-то происходит...>')


@count
def func3() -> None:
    print('<Тут что-то происходит...>')


func()
print(f'Функция {func.__name__} вызвана {func.count} - ый раз')
func()
print(f'Функция {func.__name__} вызвана {func.count} - ый раз')
func()
print(f'Функция {func.__name__} вызвана {func.count} - ый раз')
func2()
print(f'Функция {func2.__name__} вызвана {func2.count} - ый раз')
func2()
print(f'Функция {func2.__name__} вызвана {func2.count} - ый раз')
func2()
print(f'Функция {func2.__name__} вызвана {func2.count} - ый раз')
func3()
print(f'Функция {func3.__name__} вызвана {func3.count} - ый раз')
func3()
print(f'Функция {func3.__name__} вызвана {func3.count} - ый раз')