from random import randint


# 递归正序遍历数组
def recursivelist1(items, index):
    if index < len(items):
        print(items[index], end=' ')
        recursivelist1(items, index + 1)


# 递归逆序遍历数组
def recursivelist2(items, index):
    if index < len(items):
        recursivelist2(items, index + 1)
        print(items[index], end=' ')


if __name__ == '__main__':
    p = [randint(1, 100) for _ in range(7)]
    print(p)
    recursivelist1(p, 0)
    print()
    recursivelist2(p, 0)