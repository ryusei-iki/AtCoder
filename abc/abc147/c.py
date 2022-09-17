N=int(input())

A=[0]*N
x=[]
y=[]
g=[[-1 for i in range(15)] for j in range(15)]
for i in range(N):
    A[i]=int(input())
    for j in range(A[i]):
        X,Y=map(int,input().split())
        g[i][X-1]=Y

for i in range(1<<N):
    k=0
    [0 for i in range(N)]
    for j in range(N):
        if((i>>j) & 1 ==1):
            katei[k]=g[j]
            k=k+1

print(A)
print(x)
print(y)
