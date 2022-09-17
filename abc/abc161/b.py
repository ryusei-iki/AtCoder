N,M=map(int,input().split())
A=[int(i) for i in input().split()]

wa=sum(A)
count=0
for i in A:
    if(i>=1/(4*M)*wa):
        count=count+1
if(count>=M):
    print('Yes')
else:
    print('No')
