

A,B,C,D=map(int,input().split())
if(A<=C and C<= B):
    print('Yes')
    exit()
elif(C<=A and A<=D):
    print('Yes')
    exit()
else:
    print('No')
