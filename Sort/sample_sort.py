from time import time
from threading import Thread
from random import randint


# 简单的选择排序
def select_sort(origin_list, cmp = lambda x, y: x < y):
    ans_list = origin_list[:]
    ans_list = list(ans_list)
    for i in range(len(ans_list)):
        min_index = i
        for j in range(i + 1, len(ans_list)):
            if cmp(ans_list[j], ans_list[min_index]):
                min_index = j
        if min_index != i:
            ans_list[i], ans_list[min_index] = ans_list[min_index], ans_list[i]
    return ans_list


# 简单的冒泡排序
def sample_bubble_sort(origin_list, cmp = lambda x, y: x < y):
    ans_list = origin_list[:]
    ans_list = list(ans_list)
    for i in range(len(ans_list)):
        for j in range(len(ans_list) - 1, i, -1):
            if cmp(ans_list[j], ans_list[j - 1]):
                ans_list[j], ans_list[j - 1] = ans_list[j - 1], ans_list[j]
    return ans_list


# 高质量的冒泡排序(每一遍历的时候，都遍历两次，一遍从前往后，另外一遍从后往前，
# 同事判断是否已经进行了交换，如果交换了，那表示排序完了，排序结束)
def hype_bubble_sort(origin_list, cmp = lambda x, y: x < y):
    ans_list = origin_list[:]
    ans_list = list(ans_list)
    for i in range(len(ans_list) - 1):
        is_swap = False
        for j in range(i, len(ans_list) - 1 - i):
            if cmp(ans_list[j + 1], ans_list[j]):
                ans_list[j], ans_list[j + 1] = ans_list[j + 1], ans_list[j]
                is_swap = True
        if is_swap:
            is_swap = False
            for j in range(len(ans_list) - 2 - i, i, -1):
                if cmp(ans_list[j], ans_list[j - 1]):
                    ans_list[j], ans_list[j - 1] = ans_list[j - 1], ans_list[j]
                    is_swap = True
        if not is_swap:
            break
    return ans_list


# 快速排序
def quick_sort(origin_list, cmpp = lambda x, y: x < y):
    ans_list = origin_list[:]
    ans_list = list(ans_list)
    fir_quick_sort(ans_list, 0, len(ans_list) - 1)
    return ans_list


def fir_quick_sort(list, l, r):
    if l >= r:
        return
    left, right = l, r
    base = list[left]
    while l < r:
        while l < r and list[r] > base:
            r -= 1
        if l < r:
            list[l] = list[r]
        while l < r and list[l] <= base:
            l += 1
        if l < r:
            list[r] = list[l]
    list[l] = base
    fir_quick_sort(list, left, l - 1)
    fir_quick_sort(list, l + 1, right)


class TimeTestThread(Thread):

    def __init__(self, sort_func, *args):
        super().__init__()
        self._sort_func = sort_func
        self._args = args

    def run(self):
        print(self._sort_func, self._sort_func(self._args))

    def __str__(self):
        return str(self._sort_func)


def time_test():
    test_list = [randint(-100000, 100000) for _ in range(10000)]
    func_name = [select_sort, sample_bubble_sort, hype_bubble_sort, quick_sort]
    threads = []
    for i in range(4):
        t = TimeTestThread(func_name[i], *test_list)
        threads.append(t)
        t.start()
    start = time()
    for t in threads:
        t.join()
    end = time()
    print(end - start)


if __name__ == '__main__':
    # time_test()
    p = [randint(-100000, 100000) for _ in range(1000000)]
    start = time()
    fir_quick_sort(p, 0, len(p) - 1)
    end = time()
    print(p)
    print(end - start)