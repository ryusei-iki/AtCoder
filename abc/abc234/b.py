#@
n=int(input())
x=[0]*n
y=[0]*n
for i in range(n):
    x[i],y[i]=map(int,input().split())
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        ans=max(((x[i]-x[j])**2+(y[i]-y[j])**2)**(0.5),ans)

print(ans)
