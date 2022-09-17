import math
import numpy as np
N,K=map(int,input().split())
a=[0]*N
a=list(map(int,input().split()))
A=np.array(a)
b=np.zeros(N)
for i in range(K):
    if(K*N==np.sum(A)):
        break
    b=np.zeros(N)
    for j in range(N):

        minmin=max(0,math.ceil(j-A[j]-0.5))

        maxmax=min(N,math.floor(j+A[j]+0.5)+1)

        if(minmin==maxmax):
            maxmax=maxmax+1
            if(N<=maxmax):
                minmin=N-1
                maxmax=N

        for k in range(minmin,maxmax):
            b[k]=b[k]+1

    A=b
A=A.astype(np.int)
da=list(A)
L=[str(a) for a in da]

da=" ".join(L)
print(da)
