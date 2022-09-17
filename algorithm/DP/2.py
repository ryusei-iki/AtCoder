N=int(input())
w=[0]*N
v=[0]*N
for i in range(N):
    w[i],v[i]=map(int,input().split())

W=int(input())

print(N)
print(w)
print(v)
print(W)


dp=[[0 for i in range(W+1)] for i in range(N+1)]

for i in range(1,N+1):
    for j in range(W+1):
        if(0<=j-w[i-1]):
            #print(j)
            dp[i][j]=max(dp[i-1][j-w[i-1]]+v[i-1],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[N][W])
