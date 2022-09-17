#全探索
import math
n=int(input())

a=[0]*n
p=[0]*n
x=[0]*n
for i in range(n):
    a[i],p[i],x[i]=map(int,input().split())
ans=float('inf')

for i in range(n):

    if(0.5<math.ceil(a[i])-a[i]):

        if(1<=x[i]-a[i]+1):
            ans=min(ans,p[i])
    else:
        if(1<=x[i]-a[i]):
            ans=min(ans,p[i])
if(ans==float('inf')):
    print(-1)
    exit()
print(ans)
