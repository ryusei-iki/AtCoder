
#全探索
h,w=map(int,input().split())

a=[0]*h

for i in range(h):
    a[i]=list(map(int,input().split()))
mi=10**5
for i in a:

    for j in i:
        mi=min(mi,j)
ans=0

for i in a:
    for j in i:
        ans=ans+(j-mi)
print(ans)
