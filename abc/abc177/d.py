#Union-Find
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

N,M=map(int,input().split())
A=[0]*M
tomo=[ [] for i in range(N)]
for i in range(M):
    A[i]=list(map(int,input().split()))

uf=UnionFind(N+1)
for i in range(len(A)):
    uf.union(A[i][0],A[i][1])



print(abs(min(uf.parents)))
