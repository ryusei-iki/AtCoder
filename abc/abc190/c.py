#bit全探索
n,m=map(int,input().split())
a=[0]*m
b=[0]*m
for i in range(m):

    a[i],b[i]=map(int,input().split())
k=int(input())
c=[0]*k
d=[0]*k
for i in range(k):
    c[i],d[i]=map(int,input().split())
ans=0
for i in range(2**k):
    kari=0
    lis=[0]*n
    for j in range(k):

        if((i>>j)&1):
            lis[c[j]-1]=1
        else:
            lis[d[j]-1]=1

    for j in range(m):

        if(lis[a[j]-1]==1 and lis[b[j]-1]==1):
            kari=kari+1
    ans=max(ans,kari)
print(ans)
