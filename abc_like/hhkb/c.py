N=int(input())

p=list(map(int,input().split()))

check=[-1]*(200009)

mi=0
for j in range(N):
    check[p[j]]=1
    for i in range(mi,200009):
        if(check[i]!=1):
            print(i)
            mi=i
            break
