#defaultdict
#set
n,m=map(int,input().split())
s=list(map(str,input().split()))
t=list(map(str,input().split()))

from collections import defaultdict
d=defaultdict(lambda:0)
for i in range(m):
    d[t[i]]=1
for i in range(n):
    if(d[s[i]]==1):
        print('Yes')
    else:
        print('No')
