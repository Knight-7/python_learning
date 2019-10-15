from random import randint


# 筛选1000以内内被3和5整除， 但不能被7整除
def filter_use():
    p = filter(lambda x: x % 3 == 0 and x % 7 == 0, range(1000))
    p = filter(lambda x: x % 5, p)
    for i in p:
        print(i, end=' ')


def map_use():
    p = map(lambda x: x ** 2, range(10))
    for i in p:
        print(i, end=' ')


if __name__ == '__main__':
    filter_use()
    print()
    map_use()