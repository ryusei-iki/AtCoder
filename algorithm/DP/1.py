
N=int(input())

a=list(map(int,input().split()))


print(N)
print(a)

dp=[0 for i in range(N+1)]



for i in range(1,N+1):
    print(i)
    dp[i]=max(dp[i-1]+a[i-1],dp[i-1])
print(dp[N])
