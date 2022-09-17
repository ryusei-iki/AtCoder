#再帰
#dfs
import sys
sys.setrecursionlimit(200000)
n=int(input())
tka=[0]*n
for i in range(n):
    tka[i]=list(map(int,input().split()))
syutoku=[-1]*n

def sagasu(n):
    if(tka[n-1][1]==0):
        syutoku[n-1]=1

        return
    for i in range(2,tka[n-1][1]+2):
        if(syutoku[tka[n-1][i]-1]==1):
            pass
        else:

            sagasu(tka[n-1][i])

    syutoku[n-1]=1
    return

sagasu(n)
ans=0
for i in range(n):
    if(syutoku[i]==1):
        ans=ans+tka[i][0]
print(ans)
