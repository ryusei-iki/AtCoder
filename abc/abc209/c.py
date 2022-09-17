#全探索
n=int(input())
c=list(map(int,input().split()))
c=sorted(c)

ans=c[0]

for i in range(1,n):

    nn=c[i-1]
    a=c[i]-(c[i-1])
    l=c[i]-1
    if(c[i]==ans and c[i]==1):
        ans=0
        print(ans)
        exit()
    if(c[i]==i):
        pass
    if(c[i]<i):
        ans=0
        print(ans)
        exit()
    else:
        ans=(ans*(c[i]-i))%(10**9+7)

print(ans)
