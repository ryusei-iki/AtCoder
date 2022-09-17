N,K=map(int,input().split())
A=[int(i) for i in input().split()]
B=[-1 for i in range(N+1)]
C=[0 for i in range(N)]

B[1]=1
i=0

C[0]=1
for i in range(1,N+1):

    if(B[A[C[i-1]-1]]==-1):

        B[A[C[i-1]-1]]=A[C[i-1]-1]
        C[i]=A[C[i-1]-1]




    else:
        bfirst=C.index(A[C[i-1]-1])
        blast=i

        roop=blast-bfirst

        ans=(K-bfirst)%roop

        print(C[bfirst+ans])

        exit()
