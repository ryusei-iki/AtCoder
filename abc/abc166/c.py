N,M=map(int,input().split())
H=[int(i) for i in input().split()]
A=[0]*M
B=[0]*M
for i in range(M):
    A[i],B[i]=map(int,input().split())
D=[i+1 for i in range(N)]
C=[]
for i in range(M):

    if(H[A[i]-1]>H[B[i]-1]):

        C.append(B[i])

    elif(H[A[i]-1]<H[B[i]-1]):

        C.append(A[i])
    else:

        C.append(A[i])
        C.append(B[i])

G=list(set(D)-set(C))
print(len(G))
