N=int(input())
A=list(map(int,input().split()))
b=A[0]

if(A.count(0)!=0):
    print('0')
    exit()

for i in range(1,len(A)):
    b=b*A[i]
    if(10**18<b):

        print('-1')
        exit()
        
print(b)
