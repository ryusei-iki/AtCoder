#全探索 整数 いもす法
N=int(input())
a=[0]*N
b=[0]*N

for i in range(N):
    a[i],b[i]=map(int,input().split())

ans=0
for i in range(N):
    ans=ans+(b[i]-a[i]+1)*(a[i]+b[i])/2

print(int(ans))
