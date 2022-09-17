N,M,K=map(int,input().split())
A=[]
B=[]
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=[0 for i in range(len(A)+1)]
for i in range(1,len(A)+1):
    a[i]=a[i-1]+A[i-1]

b=[0 for i in range(len(B)+1)]
for i in range(1,len(B)+1):
    b[i]=b[i-1]+B[i-1]

j=M
ans=0
for i in range(len(A)+1):

    if(K<a[i]):
        break
    #print(a[i]+b[j])
    while(a[i]+b[j]>K):
        j=j-1
    ans=max(ans,i+j)

print(ans)
