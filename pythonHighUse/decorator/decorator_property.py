class Goods():
    """定义一个关于商品的类"""

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price


if __name__ == '__main__':
    g = Goods(34)
    g.price = 43
    print(g.price)
    del g.price
    print(g.price)