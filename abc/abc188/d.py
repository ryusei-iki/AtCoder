#累積和 いもす法

n,C=map(int,input().split())
a=[0]*n
b=[0]*n
c=[0]*n
event=[0]*(n*2)
for i in range(n):
    a[i],b[i],c[i]=map(int,input().split())

for i in range(0,n):
    event[i*2]=[a[i]-1,c[i]]
    event[i*2+1]=[b[i],-c[i]]



event.sort()


ans=0
fee=0
t=0

for x,y in event:
    if(x!=t):
        ans=ans+min(C,fee)*(x-t)
        t=x
    fee=fee+y
print(ans)
