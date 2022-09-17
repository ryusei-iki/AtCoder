N,X,Y=map(int,input().split())
b=[0 for i in range(N+1)]
#print(b)
for i in range(1,N):
    for j in range(i+1,N+1):
        #print('{},{}'.format(i,j))
        minmin=min([abs(j-i),abs(X-i)+1+abs(Y-j)])
        #print(minmin)
        b[minmin]=1+b[minmin]

for i in range(1,N):

    print(b[i])
