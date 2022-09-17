#整数
n,m=map(int,input().split())
b=[0]*n
for i in range(n):
    b[i]=list(map(int,input().split()))

mae=-1
if(8<b[0][0]%7+m):
    print('No')
    exit()
if(b[0][0]%7==0 and m!=1):
    print('No')
    exit()
for i in range(n):
    for j in range(m):
        if(j==0):
            saisyo=b[i][j]
        if(i==0 and j==0):
            pass
        elif(b[i][j]==mae):
            pass
        else:
            print('No')
            exit()
        mae=b[i][j]+1
    mae=saisyo+7
print('Yes')
