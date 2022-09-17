N,K=map(int,input().split())
d=[0 for i in range(K)]
A=[[0 for i in range(N)] for i in range(K)]
B=[]
C=[i+1 for i in range(N) ]
for i in range(K):
    d[i]=int(input())
    A=[0 for i in range(d[i])]
    A=[int(i) for i in input().split()]
    C=list(set(C)-set(A))

print(len(C))
