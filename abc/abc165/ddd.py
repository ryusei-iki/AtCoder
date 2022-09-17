A,B,N=map(int,input().split())



a=0
max=int(A*N/B)-A*(N//B)
ma=0
if(B<N):
    ma=int(A*(B-1)/B)


if(max<ma):
    
    print(ma)

else:

    print(max)
