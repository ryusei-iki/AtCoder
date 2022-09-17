n,m=map(int,input().split())
a=[0]*m
b=[0]*m
for i in range(m):
    a[i],b[i]=map(int,input().split())



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



uf=UnionFind(n)
for i in range(m):
    uf.union(a[i]-1,b[i]-1)
print(uf.parents)
check=[0]*n
for i in range(n):
    if(0<=uf.parents[i]):
        if(check[uf.parents[i]]==0):
            roop=[j for j, x in enumerate(uf.parents) if x==uf.parents[i]]
        roop.append(uf.parents[i])

        kaku=[0]*len(roop)
        for k in range(m):
            if(a[k]-1 in roop):
                kaku[a[k]-1]=1+kaku[a[k]-1]
            if(b[i]-1 in roop):
                kaku[b[k]-1]=1+kaku[b[k]-1]
        print(kaku)
        if(kaku in 3):
            pass
        else:

        print('==============')
print(kaku)
