#ダイクストラ法
n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))


ans=[float('inf') for i in range(n)]
mae=float('inf')

ans[0]=t[0]
mae=ans[0]+s[0]
for i in range(1,2*n+1):
    if(mae<t[i%n]):
        ans[i%n]=min(ans[i%n],mae)
        mae=ans[i%n]+s[i%n]


    else:
        ans[i%n]=min(ans[i%n],t[i%n])
        mae=ans[i%n]+s[i%n]

for i in range(n):
    print(ans[i])
