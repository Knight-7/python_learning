dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
graph = [[0 for _ in range(10)] for _ in range(10)]
path = []
results = []


def dfs(x, y):
    if x == 5 and y == 9:
        graph[x][y] = '0'
        results.append(path[:])
        for p in path:
            print(p, end='->')
        print()
        for i in range(10):
            print(*graph[i])
        return
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if 0 <= nx < 10 and 0 <= ny < 10 and graph[nx][ny] == ' ':
            graph[nx][ny] = '0'
            path.append((nx, ny))
            dfs(nx, ny)
            graph[nx][ny] = ' '
            path.pop()


def main():
    for i in range(10):
        tmp = input()
        for j in range(10):
            graph[i][j] = tmp[j]
    graph[1][0] = '0'
    dfs(1, 0)
    print(f'共找到了{len(results)}条路径')
    shortes = None
    minlen = 10000000
    for result in results:
        if len(result) < minlen:
            minlen = len(result)
            shortes = result
    print('最短路径是：')
    for p in shortes:
        print(p, end='->')


if __name__ == '__main__':
    main()
