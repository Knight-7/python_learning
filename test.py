p = list(range(7))
q = list(range(7, 14))
r = list(range(14, 21))
ans = zip(p, q, r)
for x, y, z in ans:
    print(x, y, z)