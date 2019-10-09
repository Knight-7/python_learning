from random import randint


# 列表的生成式
def list_generate():
    p = [randint(1, 100) for _ in range(50)]
    p2 = [x for x in p if x % 2]
    print(p2)


# 使用生成式
def dic_generate():
    prices = {
        'AAPL': 191.88,
        'GOOG':1186.96,
        'IBM':149.24,
        'ORCL':48.44,
        'ACN':166.89,
        'FB':208.09,
        'SYMC':21.20
    }

    prices2 = {key: value for key, value in prices.items() if value > 100}
    print(prices2)


# 嵌套的列表（二位数组）
def two_digit_array():
    wrong_p = [[None] * 3] * 4
    wrong_p[1][1] = 4
    print(wrong_p)
    true_p = [[None] * 3 for _ in range(4)]
    true_p[0][0] = 34
    print(true_p)


if __name__ == '__main__':
    two_digit_array()