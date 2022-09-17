#dfs
n, m = map(int, input().split())
k = [0] * m
a = [0] * m
for i in range(m):
    k[i] = int(input())
    a[i] = list(map(int, input().split()))

lis = [-1] * n
arr = [[] for i in range(n)]

tugimiru = [i for i in range(m)]

hukasa = [0 for i in range(m)]
# print(tugimiru)
# print(hukasa)
# print(lis)
# print('============')
while (1):
    if (len(tugimiru) == 0):
        break
    miru = tugimiru
    tugimiru = []
    for i in miru:

        if (lis[a[i][hukasa[i]] - 1] != -1):
            if (k[lis[a[i][hukasa[i]] - 1]] == hukasa[lis[a[i][hukasa[i]] - 1]] + 1 and k[i] == hukasa[i] + 1):  # 両方底に行くとき
                hukasa[lis[a[i][hukasa[i]] - 1]] = hukasa[lis[a[i][hukasa[i]] - 1]] + 1
                hukasa[i] = hukasa[i] + 1
                # print('ue')
            elif (k[i] == hukasa[i] + 1):  # 先のが底に行くとき
                hukasa[lis[a[i][hukasa[i]] - 1]] = hukasa[lis[a[i][hukasa[i]] - 1]] + 1
                tugimiru.append(lis[a[i][hukasa[i]] - 1])
                hukasa[i] = hukasa[i] + 1
                # print('man')
            elif (k[lis[a[i][hukasa[i]] - 1]] == hukasa[lis[a[i][hukasa[i]] - 1]] + 1):  # 後のが底に行くとき
                hukasa[lis[a[i][hukasa[i]] - 1]] = hukasa[lis[a[i][hukasa[i]] - 1]] + 1
                hukasa[i] = hukasa[i] + 1
                tugimiru.append(i)
                # prnt('naka')
            else:  # どこも底に行かないとき
                hukasa[lis[a[i][hukasa[i]] - 1]] = hukasa[lis[a[i][hukasa[i]] - 1]] + 1
                tugimiru.append(i)
                tugimiru.append(lis[a[i][hukasa[i]] - 1])
                hukasa[i] = hukasa[i] + 1
                # print(i)
                # print('sita')
        else:
            lis[a[i][hukasa[i]] - 1] = i
#     print(tugimiru)
#     print(hukasa)
#     print(lis)
#     print()
# print(sum(hukasa))
# print(sum(k))
if (sum(hukasa) == sum(k)):
    print('Yes')
else:
    print('No')
