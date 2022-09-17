from decimal import Decimal

N=int(input())
A=[0]*N
for i in range(N):
    A[i]=Decimal(input())
ans=0
for i in range(N):
    for j in range(i+1,N):
        if(A[i]*A[j]==int(A[i]*A[j])):
            ans+=1
print(ans)
