
s=input()

namae='chokudai'

dp=[[0 for j in range(8+1)] for i in range(len(s)+1)]
for i in range(len(s)+1):
    dp[i][0]=1
for i in range(1,len(s)+1):
    for j in range(1,8+1):
        if(s[i-1]==namae[j-1]):
            dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%(10**9+7)
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1]%(10**9+7))
