
X,N=map(int,input().split())
p=[0]*N
p=list(map(int,input().split()))
mixmix=float('inf')
hozon=-1
if(p.count(X)!=1):
    print(X)
    exit()
for i in range(1,101):
    if(p.count(X-i)!=1):
        print(X-i)
        exit()
    elif(p.count(X+i)!=1):
        print(X+i)
        exit()
