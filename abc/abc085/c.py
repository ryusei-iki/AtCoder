N,Y=map(int,input().split())

for i in range(N+1):
    for j in range(N-i+1):
        if(Y==i*10000+j*5000+(N-i-j)*1000):
            print('{i} {j} {k}'.format(i=i,j=j,k=N-i-j))
            exit()
print('-1 -1 -1')
