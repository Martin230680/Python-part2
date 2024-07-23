
from typing import Generator, Iterator


def ganaration(N: int) -> Generator[int, None, None]:
    for i in range(1, N + 1):
        result: int = i ** 2
        yield result


class Generations:
    def __init__(self, N: int):
        self.N: int = N
        self.count: int = 0
        self.result: int = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        self.count += 1
        if self.count > self.N:
            raise StopIteration
        self.result = self.count ** 2
        return self.result



N: int = int(input('Введите число N: '))
print('************** 1 способ **************')
result: Generations = Generations(N)
for i in result:
    print(i)
print('************** 2 способ **************')
for i in ganaration(N):
    print(i)
print('************** 3 способ **************')
result = (num ** 2 for num in range(1, N + 1))
for i in result:
    print(i)