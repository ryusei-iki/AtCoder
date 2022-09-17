A,B,C,D=map(int,input().split())

if(abs(C/B+1)<=abs(A/C+1)):
    print('Yes')

else:
    print('No')
