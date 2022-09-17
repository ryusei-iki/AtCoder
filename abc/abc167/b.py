A,B,C,K=map(int,input().split())


if(K<=A):
    a=K
    print(a)
    exit()
else:
    a=A
    if(A+B>=K):
        print(a)
        exit()
    else:
        if(A+B+C>=K):
            print(a-(K-A-B))
            exit()
        else:
            print(a-C)
