def fib(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


class Fib():
    """迭代器"""

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.index += 1
            return self.a
        raise StopIteration()


def main():
    for i in fib(10):
        print(i, end=' ')
    f = Fib(10)
    print()
    for i in f:
        print(i, end=' ')


if __name__ == '__main__':
    main()