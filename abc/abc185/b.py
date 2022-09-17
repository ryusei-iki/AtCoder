#全探索
n,m,t=map(int,input().split())
a=[0]*m
b=[0]*m
for i in range(m):
    a[i],b[i]=map(int,input().split())
but=n
mae=0
for i in range(m):
    but=but-(a[i]-mae)
    if(but<=0):
        print('No')
        exit()
    else:
        mae=b[i]
        but=min(but+(b[i]-a[i]),n)
but=but-(t-b[i])
if(but<=0):
    print('No')
else:
    print('Yes')
