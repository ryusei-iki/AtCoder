#dict
#defaultdict
n=int(input())
x=[0]*n
y=[0]*n
for i in range(n):
    x[i],y[i]=map(int,input().split())

from collections import defaultdict
p_exist=defaultdict(int)
for i in range(n):
    p_exist[(x[i],y[i])]=1
ans=0

for i in range(n-1):
    for j in range(i+1,n):
        if(x[i]==x[j] or y[i]==y[j]):
            continue
        if(p_exist[(x[i],y[j])]==1 and p_exist[(x[j],y[i])]==1):
            ans=ans+1

print(ans//2)
