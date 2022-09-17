







N=int(input())

a=list(map(int,input().split()))
m=list(map(int,input().split()))

A=int(input())






dp=[[-1 for i in range(A+1)] for j in range(N+1)]
dp[0][0]=0

  #DP
for i in range(N):
    for j in range(A+1):
        if (dp[i][j]>=0):
            dp[i+1][j]=m[i]
        elif (j<a[i] or dp[i+1][j-a[i]]<=0):
            dp[i+1][j]=-1
        else:
            dp[i+1][j]=dp[i+1][j-a[i]]-1


print(dp)
if(0<=dp[N][A]):
    print('True')
else:
    print('False')
print(dp[N][A])
