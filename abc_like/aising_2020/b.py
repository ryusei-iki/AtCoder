N=int(input())

a=[0]*N
a=list(map(int,input().split()))
ans=0
for i in range(1,N+5,2):
    if(N<i):
        break
    if(a[i-1]%2==1):
        ans=ans+1
print(ans)
