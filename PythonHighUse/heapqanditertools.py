import heapq
import itertools


def heapq_test():
    """
    从列表中找出最大或最小的N个元素
    堆结构（大根对/小根堆）
    """
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x:x['price']))
    print(heapq.nsmallest(2, list2, key=lambda x: x['price']))


def itertools_test():
    """
    迭代工具-排列/组合/笛卡尔积
    :return:
    """
    itertools.permutations('ABCD')  # 生成'ABCD'的排列的可迭代对象
    itertools.combinations('ABCDE', 3)  # 生成'ABCDE'这5个字母长度为3的组合的可迭代对象
    itertools.product('ABCD', '123')   #生成'ABCD'和'123'的笛卡尔积的可迭代对象


if __name__ == '__main__':
    heapq_test()
    itertools_test()