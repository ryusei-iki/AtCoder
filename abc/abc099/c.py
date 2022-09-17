#dp
n=int(input())
dp=[-1 for i in range(n+1)]

dp[0]=0

lis=[1]
i=1
while(1):
    if(n<6**i):
        break
    else:
        lis.append(6**i)
    i=i+1
i=1
while(1):
    if(n<9**i):
        break
    else:
        lis.append(9**i)
    i=i+1

for i in range(1,n+1):
    for j in range(len(lis)):
        if(0<=i-lis[j]):
            if(dp[i-lis[j]]!=-1):
                if(dp[i]!=-1):
                    dp[i]=min(dp[i-lis[j]]+1,dp[i])
                else:
                    dp[i]=dp[i-lis[j]]+1
print(dp[-1])
