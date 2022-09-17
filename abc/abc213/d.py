#dfs
import sys
sys.setrecursionlimit(300000)
n=int(input())
a=[0]*(n-1)
b=[0]*(n-1)
for i in range(n-1):
    a[i],b[i]=map(int,input().split())

seen=[0]*n
seen_modori=[0]*n
lis=[[] for i in range(n)]
# print(lis)
for i in range(n-1):
    lis[a[i]-1].append(b[i]-1)
    lis[b[i]-1].append(a[i]-1)
# print(lis)
for i in range(n):
    lis[i]=sorted(lis[i])
# print(lis)

def dfs(goal,start):
    seen[start]=True
    print(start+1)
    for i in lis[start]:
        if(seen[i]==False):
            seen[i]=True
            dfs(goal,i)
            print(start+1)


seen[0]=True
dfs(n,0)
