# 快速排序
def quick_sort(origin_list, kind = 1):
    ans_list = origin_list[:]
    ans_list = list(ans_list)
    if kind == 1:
        fir_quick_sort(ans_list, 0, len(ans_list) - 1)
    elif kind == 2:
        sec_quick_sort(ans_list, 0, len(ans_list) - 1)
    return ans_list


# 传统的快速排序
def fir_quick_sort(list, l, r, cmp = lambda x, y: x < y):
    if l >= r:
        return
    left, right = l, r
    base = list[left]
    while l < r:
        while l < r and cmp(base, list[r]):
            r -= 1
        if l < r:
            list[l] = list[r]
        while l < r and (cmp(list[l], base) or list[l] == base):
            l += 1
        if l < r:
            list[r] = list[l]
    list[l] = base
    fir_quick_sort(list, left, l - 1, cmp)
    fir_quick_sort(list, l + 1, right, cmp)


# 有些略微优化的快速排序
def sec_quick_sort(list, l, r):
    if l >= r:
        return
    if l + 10 >= 10:
        left, right = l, r
        base = list[left]
        while l < r:
            while l < r and list[r] >= base:
                r -= 1
            if l < r:
                list[l] = list[r]
            while l < r and list[l] <= base:
                l += 1
            if l < r:
                list[r] = list[l]
        list[l] = base
        sec_quick_sort(list, left, l - 1)
        sec_quick_sort(list, l + 1, right)
    else:
        for i in range(l, r + 1):
            for j in range(l, 0, -1):
                if list[l] < list[l - 1]:
                    list[l], list[l - 1] = list[l - 1], list[l]
                else:
                    break


if __name__ == '__main__':
    pass