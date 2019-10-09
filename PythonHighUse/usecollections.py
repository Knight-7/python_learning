from collections import Counter, deque
from random import randint


def counter_test():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = Counter(words)
    print(counter)
    for i in range(1, len(counter) + 1):
        print(counter.most_common(i))


def deque_test():
    dq = deque()
    for _ in range(7):
        tmp = randint(1, 100)
        if len(dq) == 0:
            dq.append(tmp)
        elif tmp <= dq[0]:
            dq.appendleft(tmp)
        elif tmp >= dq[-1]:
            dq.append(tmp)
    for x in dq:
        print(x, end=" ")


if __name__ == '__main__':
    counter_test()
    deque_test()