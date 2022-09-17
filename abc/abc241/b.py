#defaultdict
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
from collections import defaultdict
d=defaultdict(lambda:0)
for i in range(n):
    d[a[i]]=d[a[i]]+1
for i in range(m):
    if(1<=d[b[i]]):
        d[b[i]]=d[b[i]]-1
    else:
        print('No')
        exit()
print('Yes')
