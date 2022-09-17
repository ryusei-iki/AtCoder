N,Q=map(int,input().split())
A=[0]*N
B=[0]*N
C=[0]*Q
D=[0]*Q
rate=[0]*(2*10**5)
for i in range(N):
    A[i],B[i]=map(int,input().split())
    rate[B[i]-1]=max(rate[B[i]-1],A[i])
for i in range(Q):
    C[i],D[i]=map(int,input().split())
mae_you=-1
for i in range(Q):
    mae_you=B[C[i]]
    if(rate[mae_you]==A[C[i]]):
        rate[]
