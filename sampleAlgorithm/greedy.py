"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""
class Thing():
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        return self.price / self.weight


def input_thing():
    name, price, weight = input().split()
    return name, int(price), int(weight)


def main():
    max_weight, num_thing = map(int, input().split())
    things = []
    for _ in range(num_thing):
        things.append(Thing(*input_thing()))
    things.sort(key=lambda x: x.value, reverse=True)
    total_price, total_weight = 0, 0
    for thing in things:
        if thing.weight + total_weight <= max_weight:
            print(f'小偷偷走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(total_price)


if __name__ == '__main__':
    main()