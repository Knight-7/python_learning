flag = True
op = [[0, 2], [2, 0], [1, 1], [1, 0], [0, 1]]
visit = []

def dfs(M, C, m, c):
    global flag
    if M < 0 or C < 0 or m < 0 or c < 0:
        return False
    if (M and C > M) or (m and c > m):
        return False
    if (flag and M == 0 and C == 0) or (not flag and m == 0 and c == 0):
        return True
    if not flag:
        s = f'M={M}, C={C}, m={m}, c={c}, boat=left'
    else:
        s = f'M={m}, C={c}, m={M}, c={C}, boat=right'
    if s in visit:
        return False
    visit.append(s)
    flag = not flag
    for i in range(5):
        if dfs(m + op[i][1], c + op[i][0], M - op[i][1], C - op[i][0]):
            print(op[i][1], op[i][0])
            print(s)
            return True
    flag = not flag
    visit.pop()
    return False


if __name__ == '__main__':
    M, C = map(int, input().split())
    m, c = 0, 0
    print(f'M={M}, C={C}, m={m}, c={c}, boat=left')
    if not dfs(M, C, m, c):
        print("Can't find the solution.")
