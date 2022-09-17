N,M,K=map(int,input().split())
A=[]
B=[]
A=list(map(int,input().split()))
B=list(map(int,input().split()))

dp=[[0 for j in range(K+1)] for i in range(max(N,M)+1)]
if(N<M):
    ma=M
    mi=N
    turn='M'
else:
    ma=N
    mi=M
    turn='N'

if(turn=='M'):
    for i in range(ma):
        for j in range(K+1):
            if(mi<=i):
                if(B[i]<j):
                    dp[i+1][j]=max(dp[i][j-B[i]]+1,dp[i][j])
                else:
                    dp[i+1][j]=dp[i][j]
            else:

                if(A[i]<j and B[i]<j):

                    dp[i+1][j]=max(dp[i][j-A[i]-B[i]]+2,dp[i][j])

                elif(A[i]<j):
                    dp[i+1][j]=max(dp[i][j-A[i]]+1,dp[i][j])
                elif(B[i]<j):
                    dp[i+1][j]=max(dp[i][j-B[i]]+1,dp[i][j])
                else:
                    dp[i+1][j]=dp[i][j]
else:
    for i in range(ma):
        for j in range(K+1):
            if(mi<=i):
                if(A[i]<j):
                    dp[i+1][j]=max(dp[i][j-A[i]]+1,dp[i][j])
                else:
                    dp[i+1][j]=dp[i][j]
            else:
                if(A[i]<j and B[i]<j):
                    dp[i+1][j]=max(dp[i][j-A[i]-B[i]]+2,dp[i][j])

                elif(A[i]<j):
                    dp[i+1][j]=max(dp[i][j-A[i]]+1,dp[i][j])
                elif(B[i]<j):
                    dp[i+1][j]=max(dp[i][j-B[i]]+1,dp[i][j])
                else:
                    dp[i+1][j]=dp[i][j]

print(dp[ma][K])
