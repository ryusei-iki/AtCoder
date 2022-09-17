#整数
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
n,m=map(int,input().split())
a=list(map(int,input().split()))
naka=[]

for i in range(n):
    da=factorization(a[i])
    for j in range(len(da)):
        if(da[0][0]==1):
            break
        naka.append(da[j][0])

naka=list(set(naka))

lis=[0]*(m+1)

for i in range(len(naka)):
    j=1
    while(naka[i]*j<=(m)):
        lis[naka[i]*j]=1
        j=j+1


print(m-sum(lis))
for i in range(1,len(lis)):
    if(lis[i]==0):
        print(i)
