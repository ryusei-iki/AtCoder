X,Y=map(int,input().split())

for i in range(X+1):
    if(Y==i*2+(X-i)*4):
        print('Yes')
        exit()
print('No')
