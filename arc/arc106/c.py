class UnionFind():
    def __init__(self, n):
        self.n = n
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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __list__(self):
        return  [self.members(r) for r in self.roots()]
    def lis(self):

        return self.roots()
        #return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=[0]*M
for i in range(M):
    c[i]=list(map(int,input().split()))
    if(c[i][1]<c[i][0]):
        temp=c[i][1]
        c[i][1]=c[i][0]
        c[i][0]=temp
print(c)
wa=[0]*N
yotei=[0]*N
uf=UnionFind(N)

for i in range(M):
    uf.union(c[i][0]-1,c[i][1]-1)
print(uf.parents)
#print(uf.__list__())
aa=uf.__list__()

for i in aa:

    wa=0
    yotei=0
    for j in i:

        wa=wa+a[j]
        yotei=yotei+b[j]
    if(wa==yotei):
        pass
    else:
        print('No')
        exit()

print('Yes')
