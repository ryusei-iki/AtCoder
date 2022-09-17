N=int(input())
A=[0]
A=list(map(int,input().split()))

A.sort(reverse=True)
wa=A[0]
i=0
amari=len(A)%2

while(1):

    if(amari==0):

        if(len(A)-1==1+2*i):
            print(wa)
            break
        wa=A[i+1]*2+wa


    elif(amari==1):
        if(len(A)-2==1+2*i):
            print(A[i+1]+wa)
            break
        wa=A[i+1]*2+wa

    i=i+1
