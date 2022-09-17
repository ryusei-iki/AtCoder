
'''
N,K=map(int,input().split())
L=[0]*K
R=[0]*K
mo=998244353
lis=[]
for i in range(K):
    L[i],R[i]=map(int,input().split())
    lis.extend(list(range(L[i],R[i]+1)))
    lis=list(set(lis))
print(lis)

# O(N**2)のdp

dp=[0 for i in range(N)]

dp[0]=1

for i in range(N-1):
    for j in range(len(lis)):
        if(0<=i+1-lis[j]):
            dp[i+1]=(dp[i+1]+dp[i+1-lis[j]])%mo
print(dp)
print(dp[-1])




'''



N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]
mod = 998244353

print(LR)

dp = [0] * N # dpテーブル
sdp = [0] * (N+1) # dpテーブルの累積和

# DPの初期値を設定
dp[0] = 1
sdp[1] = 1

for n in range(1, N):
    for lr in LR:
        print(lr[1],lr[0])
        left = max(0, n - lr[1])
        right = max(0, n - lr[0] + 1)
        print(right,left)
        dp[n] += sdp[right] - sdp[left]
        dp[n] %= mod
    sdp[n+1] = (sdp[n] + dp[n]) % mod

res = dp[N-1]
print(res)
print(sdp)
print(dp)
