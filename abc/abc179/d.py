#dp 配るdp
N,K=map(int,input().split())
L=[0]*K
R=[0]*K
lis=[]
for i in range(K):
    L[i],R[i]=map(int,input().split())
    lis.extend(list(range(L[i],R[i]+1)))
    lis=list(set(lis))
print(lis)

dp=[[0 for j in range(N+1)] for i in range(len(lis)+1)]
dp[0][0]=1
print(dp)

for i in range(len(lis)):
    for j in range(N+1):

        dp[i+1][j]=dp[i][j]
        if(lis[i]<=j):
            dp[i+1][j]=dp[i][j-lis[i]]+dp[i+1][j]

print(dp)
if(dp[-1][-1]!=0):
    print(dp[-1][-1])
