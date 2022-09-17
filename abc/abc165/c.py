N,M,Q=map(int,input().split())

a=[]*Q
b=[]*Q
c=[]*Q
d=[]*Q

print([5]+[8])
for i in range(Q):
    a,b,c,d=map(int,input().split())

suretu=[i+1 for i in range(N)]

V = [[] for _ in range(N+1)]
print(V)
# 初期値として長さ1のものを入れる
for i in range(1, M+1):
    V[1].append([i])
print(V)
print(V[1][0][0])
# V[k] から V[k+1] を作る
for i in range(1, N):
    for v in V[i]:
        # 単調増加なので、末尾の値以上であるものを全て試す
        b = v[-1]
        print(v)

        for a in range(b, M+1):
            print(v)
            print([a])
            v2 = v + [a]
            print(v2)
            exit()
            V[i+1].append(v2)



print(V[1])
