#全探索
n=int(input())
a=list(map(int,input().split()))
ans=0

lis=0
ans=a[0]
for i in range(n-1):
    lis=a[i]
    ans=max(ans,a[i])
    for j in range(i+1,n):
        lis=min(lis,a[j])
        ans=max(ans,lis*(j+1-i))
    ans=max(ans,a[n-1])

print(ans)
