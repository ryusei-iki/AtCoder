#全探索
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=list(set(a))
b=list(set(b))
n=len(a)
m=len(b)
a.sort()
b.sort()

basyo=0
ans=float('inf')
for i in range(m):#b
    for j in range(basyo,n):#a

        if(b[i]>a[j]):
            ans=min(abs(a[j]-b[i]),ans)
            basyo=j
        elif(b[i]<a[j]):
            ans=min(abs(a[j]-b[i]),ans)
            basyo=j
            break
        else:
            print(0)
            exit()

print(ans)
