
T=int(input())



N=[0]*T
A=[0]*T
B=[0]*T
C=[0]*T
D=[0]*T
for i in range(T):
    N[i],A[i],B[i],C[i],D[i]=map(int,input().split())
bairitu=[0]*4
for i in range(T):
    bairitu[0]=2.0/float(A[i])
    bairitu[1]=3.0/float(B[i])
    bairitu[2]=5.0/float(C[i])
    bairitu[3]=1/float(D[i])
    test=[0]*4
    now=0
    cost=0
    max_num=0
    test_ok=[0]*4
    while(now!=N[i]):
        test[0]=now*int(bairitu[0])
        test[1]=now*int(bairitu[1])
        test[2]=now*int(bairitu[2])
        test[3]=bairitu[3]
        for j in range(4):
            if (test[j]<=now):
                test_ok[j]=test[i]
            else:
                test_ok[j]=0
                bairitu[j]=0
        #print(test_ok)
        max_num=max(test_ok)
        max_index=test.index(max_num)
        if(max_index==1):
            now=now*2
            cost=cost+A[i]
        elif(max_index==2):
            now=now*3
            cost=cous+B[i]
        elif(max_index==3):
            now=now*5
            cost=cost+C[i]
        else:
            now=now+1
            cost=cost+D[i]
    print(cost)
