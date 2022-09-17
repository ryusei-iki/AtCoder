#全探索
N=int(input())
x=list(map(int,input().split()))

man=0
yu=0
che=0

for i in range(N):
    x[i]=abs(x[i])
    man=man+x[i]
    yu=yu+x[i]**2

    che=max(che,x[i])

print(man)
print(yu**(1/2))
print(che)
