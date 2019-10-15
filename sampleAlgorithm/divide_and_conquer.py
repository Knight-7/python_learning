"""
分治法
"""
from random import randint


def quick_sort(origin_items, cmp= lambda x, y: x <= y):
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, cmp)
    return items


def _quick_sort(items, start, end, cmp):
    if start < end:
        pos = _partition(items, start, end, cmp)
        _quick_sort(items, start, pos - 1, cmp)
        _quick_sort(items, pos + 1, end, cmp)


# 分治：从以最后一个点为依据，将比它小的放到前面，大的放在后面
def _partition(items, start, end, cmp):
    pivod = items[end]
    i = start - 1
    for j in range(start, end):
        if cmp(items[j], pivod):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


if __name__ == '__main__':
    p = [randint(1, 100) for _ in range(7)]
    print(p)
    print(quick_sort(p))