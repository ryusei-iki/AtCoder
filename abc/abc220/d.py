#dp
n=int(input())
a=list(map(int,input().split()))

dp=[[0 for i in range(10)] for j in range(n)]
dp[0][a[0]]=1

for i in range(n-1):
    for j in range(10):
        if(dp[i][j]!=0):
            f=(j+a[i+1])%10
            g=(j*a[i+1])%10
            dp[i+1][f]=(dp[i][j]+dp[i+1][f])%998244353
            dp[i+1][g]=(dp[i][j]+dp[i+1][g])%998244353

for i in range(10):
    print(dp[-1][i])
