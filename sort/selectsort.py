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


if __name__ == '__main__':
    pass