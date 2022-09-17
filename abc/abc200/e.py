n=int(input())
a=list(map(int,input().split()))
ans=int(input())
dp=[[0 for i in range(200)] for j in range(100)]
dp[0][0]=1
for i in range(n):
    for j in range(200):
        if(a[i]<=j):

            dp[i+1][j]=dp[i+1][j]+1
print(dp[i][ans])
