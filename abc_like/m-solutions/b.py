A,B,C=map(int,input().split())
K=int(input())

for i in range(0,K+1):
    for j in range(0,K+1-i):
        for k in range(0,K+1-i-j):
            #print('{},{},{}'.format(i,j,k))
            if(A*(2**i) < B*(2**j) and B*(2**j) < C*(2**k)):
                if(i==j==k==0):
                    pass
                else:
                    print('Yes')
                    exit()

print('No')
