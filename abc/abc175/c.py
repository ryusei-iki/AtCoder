X,K,D=map(int,input().split())

X=abs(X)
idou=K*D
if(0<X):
    if(K*D<X):
        print(X-K*D)
        exit()

    a=abs(X//D)
    b=abs(X//D)+1
    kyori_a=X-a*D
    kyori_b=X-b*D

    if(K-a==0):
        print(abs(kyori_a))
        exit()
    if((K-a)%2==0):
        print(abs(kyori_a))
        exit()
    else:
        print(abs(kyori_b))
        exit()

elif(X==0):
    if(K%2==0):
        print(0)
        exit()
    else:
        print(D)
        exit()
