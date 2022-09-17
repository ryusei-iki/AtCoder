#再帰
import sys
sys.setrecursionlimit(2000000)
n,x=map(int,input().split())
a=list(map(int,input().split()))
check=[0 for i in range(n)]
def miru(koko):
    if(check[a[koko]-1]==1):
        return
    else:
        check[a[koko]-1]=1
        miru(a[koko]-1)
        return

check[x-1]=1
miru(x-1)
print(sum(check))
