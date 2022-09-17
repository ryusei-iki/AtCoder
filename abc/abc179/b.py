#全探索
N=int(input())
a=[0]*N
b=[0]*N
for i in range(N):
    a[i],b[i]=map(int,input().split())
count=0
for i in range(N):
    if(a[i]==b[i]):
        count=count+1
        if(count==3):
            print('Yes')
            exit()
    else:
        count=0
print('No')
