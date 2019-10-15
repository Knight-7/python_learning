def merge_sort(items, cmp=lambda x, y: x < y):
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], cmp)
    right = merge_sort(items[mid:], cmp)
    return merge(left, right, cmp)


def merge(item1, item2, cmp):
    items = []
    index1, index2 = 0, 0
    while index1 < len(item1) and index2 < len(item2):
        if cmp(item1[index1], item2[index2]):
            items.append(item1[index1])
            index1 += 1
        else:
            items.append(item2[index2])
            index2 += 1
    items += item1[index1:]
    items += item2[index2:]
    return items


if __name__ == '__main__':
    p = [1, 34, 8, 2, 76, 67, 21]
    print(merge_sort(p))