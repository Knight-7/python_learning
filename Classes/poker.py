"""
经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
"""
from enum import Enum, unique
import random


class Suite(Enum):
    """花色"""

    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        """重载运算符，例：x < y 等价于x.__lt__(y)"""
        return self.value < other.value


class Card():
    """牌"""

    def __init__(self, suite, face):
        """初始方法"""
        self.suite = suite
        self.face = face

    def show(self):
        """显示牌面"""
        suites = ['♠️', '♥️', '♣️', '♦️']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    """str和repr的区别：http://baijiahao.baidu.com/s?id=1596817611604972751&wfr=spider&for=pc"""
    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()


class Poker():
    """扑克"""

    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """洗牌（将卡的顺序打乱）"""
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player():
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def one(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def sort(self, cmp=lambda card: (card.suite, card.face)):
        """整理手中的牌"""
        self.cards.sort(key=cmp)


def main():
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
            player.one(poker.deal())
    for player in players:
        player.sort()
        print(f'name:{player.name}:', end=':')
        print(player.cards)


if __name__ == '__main__':
    main()