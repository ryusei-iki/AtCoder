#優先度付きキュー
n,k=map(int,input().split())
p=list(map(int,input().split()))

lis=[-1]*n
for i in p[:k]:
    lis[i-1]=1

mae=0

for i in range(n-k+1):
    lis[p[i+k-1]-1]=1

    for j in range(mae,n):
        if(p[i+k-1]<mae):
            print(mae)
            break
        if(lis[j]==1):
            print(j+1)
            mae=j+1
            break
    if(mae==n):
        for k in range(n-k+1-i-1):
            print(mae)
        exit()
