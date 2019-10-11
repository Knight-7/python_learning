from random import randint


from sort.mergesort import merge_sort
from Sort.quicksort import quick_sort
from Sort.selectsort import select_sort


def test_mergesort(items, cmp = lambda x, y: x < y):
    print(merge_sort(items, cmp))


if __name__ == '__main__':
    p = [randint(-10000, 10000) for _ in range(10000)]
    print(p)
    test_mergesort(p)