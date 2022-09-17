S=input()
N=len(S)
a=[]
b=[]
c=[]
d=[]

for i in range((N-1)//2):
    if((N-1)//2%2==1):
        if((N-1)//4>i ):
            a.append(S[i])

        elif((N-1)//4!=i):
            b.append(S[i])
    else:
        if((N-1)//4>i ):
            a.append(S[i])

        elif((N-1)//4==i):
            b.append(S[i])

        elif((N-1)//4!=i):
            b.append(S[i])

if(a==b[::-1]):
    if(S==S[::-1]):

        print('Yes')
    else:
        print('No')
    exit(0)

    for i in range((N+3)//2-1,N):
        if(((N+3)//2-1+N)//2>i ):
            c.append(S[i])
        elif(((N+3)//2-1+N)//2!=i):
            d.append(S[i])
    if(c==d):
        if(S==S[::-1]):

            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')
