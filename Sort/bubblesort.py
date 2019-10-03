# 简单的冒泡排序
def sample_bubble_sort(origin_list, cmp = lambda x, y: x < y):
    ans_list = origin_list[:]
    for i in range(len(ans_list)):
        for j in range(len(ans_list) - 1, i, -1):
            if cmp(ans_list[j], ans_list[j - 1]):
                ans_list[j], ans_list[j - 1] = ans_list[j - 1], ans_list[j]
    return ans_list


# 高质量的冒泡排序(每一遍历的时候，都遍历两次，一遍从前往后，另外一遍从后往前，
# 同事判断是否已经进行了交换，如果交换了，那表示排序完了，排序结束)
def hype_bubble_sort(origin_list, cmp = lambda x, y: x < y):
    ans_list = origin_list[:]
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


if __name__ == '__main__':
    pass