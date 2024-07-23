# TODO здесь писать код
import time

def timeout(fun):
    def wrapped_fun():
        time.sleep(10)
        result = fun()
        return result
    return wrapped_fun


@timeout
def fun():
    print('<Тут что-то происходит...>')
@timeout
def fun1():
    print('<Тут что-то происходит...>')

@timeout
def fun2():
    print('<Тут что-то происходит...>')

fun()
fun1()
fun2()