import itertools

N,M,X=map(int,input().split())
C=[]*N


A=[]
seq=[]
for i in range(N):
    A.append(list(map(int,input().split())))
    seq.append(i)
rikai=[0 for i in range(M+1)]

min=-1
count=0


for i in range(1,N+1):
    kumi=list(itertools.combinations(seq,i))
    #print(kumi)
    for j in kumi:

        for n in list(j):

            for k in range(M+1):
                rikai[k]=A[n][k]+rikai[k]

        for k in range(1,len(rikai)):
            if(X<=rikai[k]):

                count=count+1

            rikai[k]=0
        if(count==len(rikai)-1):

            if(rikai[0]<min or min==-1):
                min=rikai[0]

        rikai[0]=0
        count=0
print(min)
