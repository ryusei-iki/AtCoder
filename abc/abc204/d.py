#dp
n=int(input())
t=list(map(int,input().split()))
goal=sum(t)/2
dp=[[-1 for j in range(sum(t))] for i in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    for j in range(sum(t)):
        dp[i][j]=dp[i-1][j]
        if(t[i-1]<=j):

            if(dp[i-1][j-t[i-1]]==1):

                dp[i][j]=1

ans=0
for i in range(sum(t)):
    if(dp[-1][i]==1):
        kari=i
        if(abs(goal-kari)<abs(goal-ans)):
            ans=kari
print(max(ans,sum(t)-ans))






