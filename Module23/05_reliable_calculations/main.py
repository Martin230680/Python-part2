import math


def get_sage_sqrt(num):
    try:
        result = math.sqrt(num)
        print(f"Квадратный корень numbers {num}: {result}")
    except ValueError:
        print("Отрицательоне значение")
    except Exception:
        print("Некорректные данные")
    return


numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    get_sage_sqrt(number)

# зачтено
