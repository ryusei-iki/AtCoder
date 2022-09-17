#重複組合せ
#aからbまでのm個の数字の中からn個を選ぶ組合せバージョン
a,b,m,n=map(int,input().split())
permutation=[0]*3
def dfs(minn,maxx,size,depth):
    if(depth==size):
        print(*permutation,sep='')
    else:
        for i in range(maxx-minn+1):
            permutation[depth]=minn+i
            dfs(minn+i,maxx,size,depth+1)

dfs(a,b,n,0)
