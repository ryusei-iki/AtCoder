N,M,K=map(int,input().split())
A=[]
B=[]
A=list(map(int,input().split()))
B=list(map(int,input().split()))
goukei=[[0 for i in range(M+1)] for i in range(N+1)]
for i in range(1,N+1):
    goukei[i][0]=goukei[i-1][0]+A[i-1]
maxmax=0



for i in range(1,N+1):

    for j in range(1,M+1):
        goukei[i][j]=goukei[i][j-1]+B[j-1]
        if(K<goukei[i][j]):
            break
        else:
            maxmax=i+j

print(maxmax)
