K,N=map(int,input().split())
a=[int(i) for i in input().split()]
a.append(a[0])

max=0
b=0
for i in range(N-1):
    b=a[i+1]-a[i]
    if(b>=max):
        max=b
    
m=K-a[i+1]+a[0]

if(m>max):
    max=m

kyori=K-max

print(kyori)
