class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x


uf = UnionFind(5)
print(uf.parents)
# [-1, -1, -1, -1, -1]

uf.union(3, 4)
print(uf.parents)
uf.union(0,1)
print(uf.parents)
uf.union(1, 2)
print(uf.parents)
uf.union(0, 4)
print(uf.parents)











#
# N,M=map(int,input().split())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
#
# c=[0]*M
# for i in range(M):
#     c[i]=list(map(int,input().split()))
#
#
# wa=[0]*N
# yotei=[0]*N
# uf=UnionFind(N)
#
# for i in range(M):
#     uf.union(c[i][0]-1,c[i][1]-1)
#     print(uf.parents)
#
# con=0
# print(uf.parents)
#
# for i in list(uf.parents):
#     print(i)
#     if(0<i):
#
#         wa[i]=wa[i]+a[con]
#         yotei[i]=yotei[i]+b[con]
#     else:
#
#         wa[con]=wa[con]+a[con]
#         yotei[con]=yotei[con]+b[con]
#     print(wa)
#     print(yotei)
#     con=con+1
#
# for i in range(len(wa)):
#     if(wa[i]==yotei[i]):
#         pass
#     else:
#         print('No')
#         exit()
#
# print('Yes')
