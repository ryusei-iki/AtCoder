#全探索
n=int(input())
x=[0]*n
for i in range(n):
    x[i]=list(map(int,input().split()))

ans=0
for i in range(n-1):
    for j in range(i+1,n):
        if(abs((x[j][1]-x[i][1])/(x[j][0]-x[i][0]))<=1):
            ans=ans+1
print(ans)
