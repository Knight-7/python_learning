from random import randint




def seq_seach(items, key):
    """顺序查找"""
    for index, item in enumerate(items): # enumerate函数的作用是将可遍历对象组合为索引序列，即得到一个编号+内容的组合
        if item == key:
            return index
    return -1


def bin_search(items, key):
    """对分查找"""
    l, r = 0, len(items)
    while l <= r:
        mid = (l + r) // 2
        if items[mid] == key:
            return mid
        elif items[mid] > key:
            r = mid - 1
        else:
            l = mid + 1
    return -1


if __name__ == '__main__':
    p = [randint(0, 1000) for _ in range(500)]