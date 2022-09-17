N=int(input())
K=int(input())
a=list(map(int,input().split()))

A=int(input())

dp=[[float('inf') for i in range(A+1)] for i in range(N+1)]
dp[0][0]=0


for i in range(N):

    for j in range(A+1):
        dp[i+1][j]=min(dp[i+1][j],dp[i][j])
        if(0<=j-a[i]):
            dp[i+1][j]=min(dp[i][j-a[i]]+1,dp[i+1][j])


if(dp[N][A]<=K):
    print('Yes')
else:
    print('No')
