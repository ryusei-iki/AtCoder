#重複順列
#aからbまでのm個の数字の中からn個を選ぶ
a,b,m,n=map(int,input().split())
permutation=[0]*3
def dfs(minn,maxx,size,depth):
    if(depth==size):
        print(*permutation,sep='')
    else:
        for i in range(maxx-minn+1):
            if(used[i]==False):
                permutation[depth]=minn+i
                used[i]=True
                dfs(minn,maxx,size,depth+1)
                used[i]=False
            else:
                pass
used=[False]*m
dfs(a,b,n,0)
