N,D=map(int,input().split())
X=[0]*N
Y=[0]*N
for i in range(N):
    X[i],Y[i]=map(int,input().split())
ans=0
for i in range(N):
    if((X[i]**2+Y[i]**2)**(1/2)<=D):
        ans=ans+1

print(ans)
