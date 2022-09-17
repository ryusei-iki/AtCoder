A=[]
for i in range(3):
    A.append(list(map(int,input().split())))

N=int(input())
b=[0 for i in range(N)]
for i in range(N):
    b[i]=int(input())


for i in range(3):
    if(A[i][0] in b and A[i][1] in b and A[i][2] in b):
        print('Yes')
        exit()
    if(A[0][i] in b and A[1][i] in b and A[2][i] in b):
        print('Yes')
        exit()
if(A[0][0] in b and A[1][1] in b and A[2][2] in b):
    print('Yes')
    exit()
if(A[0][2] in b and A[1][1] in b and A[2][0] in b):
    print('Yes')
    exit()

print('No')
