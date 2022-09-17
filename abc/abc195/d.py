n,m,q=map(int,input().split())
w=[0]*n
v=[0]*n
for i in range(n):
    w[i],v[i]=map(int,input().split())
x=list(map(int,input().split()))
query=[[] for i in range(q)]
query=[0]*q
print(x)
for i in range(q):
    query[i]=list(map(int,input().split()))



print(query)

dp=[[[0 for i in range(sum(v))] for j in range(m)] for k in range(n)]

dp=[[0 for i in range(m)] for j in range(n)]
dp_basyo=[[[0]*m for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if(w[i]<=x[j]):
            if(dp_basyo[i][j]==0):
                dp[i][j]=dp[i-1][j]+v[i]
            else:
                if(dp[i-1][j]<dp[i-1][j-v[i]]+v[i]):
                    dp[i][j]=dp[i-1][j-v[i]+v[i]]
                    dp[i][j]=
                else:
                    dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j]
            dp_basyo[i][j]=dp[i-1][j]




