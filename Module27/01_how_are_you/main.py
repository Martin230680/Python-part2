from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        input('Как дела?: ')
        print('А у меня не очень! А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result

    return wrapped_func


@how_are_you
def func() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def func1() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def func2() -> None:
    print('<Тут что-то происходит...>')


func()
func1()
func2()
