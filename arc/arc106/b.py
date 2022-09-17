
N,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=[0]*M
for i in range(M):
    c[i]=list(map(int,input().split()))


if(sum(a)==sum(b)):
    print('Yes')
else:
    print('No')


d=a[1]
print(d)
e=b[1]
print(e)
d=a[1]+a[3]
print(d)
e=b[1]+b[3]
print(e)
d=a[0]+a[2]+a[8]+a[10]+a[4]+a[14]
print(d)
e=b[0]+b[2]+b[8]+b[10]+b[4]+b[14]
print(e)
dd=0
ee=0
for i in [0,2,4,8,10,14]:
    dd=dd+a[i]
    ee=ee+b[i]
    print(dd)
    print(ee)
    print()


ddd=0
eee=0
for i in [1,3,9]:
    ddd=ddd+a[i]
    eee=eee+b[i]
    print(ddd)
    print(eee)
