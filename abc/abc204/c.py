#dfs
import sys

sys.setrecursionlimit(10000)
n, m = map(int, input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())
check = [[] for i in range(n)]

for i in range(m):
    check[a[i] - 1].append(b[i] - 1)


def dfs(ima):
    if (temp[ima] == True):
        return 0
    temp[ima] = True
    for i in check[ima]:
        dfs(i)


ans = 0
for i in range(n):
    temp = [False] * n
    dfs(i)
    ans = ans + sum(temp)
print(ans)