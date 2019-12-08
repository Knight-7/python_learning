dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]
origin = [[2, 8, 3], [1, ' ', 4], [7, 6, 5]]
target = [[1, 2, 3], [8, ' ', 4], [7, 6, 5]]


class Node:
    def __init__(self, p, path):
        self.p = p
        self.path = path


def cmp(p1, p2):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if p1[i][j] != p2[i][j]:
                cnt += 1
    return cnt


def bfs():
    first = Node(origin, [])    # Node的两个中，p表示当前八字码的状态，path表示的是八字码之前的状态，记录的是当前八字码是如何来的
    q = [first]                 # 将Python中的队列当成了队列来使用
    states = [origin]
    while len(q) > 0:
        tmp = []
        now_q = q[0]
        q = q[1:]
        for i in range(3):
            if ' ' in now_q.p[i]:
                x = i
                y = now_q.p[i].index(' ')
        minn = 100
        for i in range(4):
            cur = [now_q.p[i][:] for i in range(3)]
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < 3 and 0 <= ny < 3:
                cur[nx][ny], cur[x][y] = cur[x][y], cur[nx][ny]
                if cur not in states:
                    tmp.append(cur)
                    states.append(cur)
                minn = min(minn, cmp(cur, target))  # 记录扩展的状态中与目标格局相比数码不同位置的个数
        if minn == 0:                               # 达到目标格局，将之前的状态和当前状态输出出来
            for c in tmp:
                if cmp(c, target) == 0:
                    for i in range(3):
                        print(*origin[i])
                    print()
                    for p in now_q.path:
                        for i in range(3):
                            print(*p[i])
                        print()
                    for i in range(3):
                        print(*c[i])
            return
        for c in tmp:                               # 择优，将与目标格局相比数码不同位置个数最小的状态加入到OPEN表中
            path = now_q.path[:]
            if cmp(c, target) == minn:
                path.append(c)
                new_node = Node(c, path)
                q.append(new_node)
        tmp.clear()


if __name__ == '__main__':
    bfs()