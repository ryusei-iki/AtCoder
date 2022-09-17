def modpow(a,n,mod):
    res=1
    while(n>0):
        if(n&1) :
            res=res*a%mod

        a=a*a%mod
        n=n >> 1
    return res
import math
def modinv(a,m):
    b=m,u=1,v=0
    while(b):
        t=a/b
        a-=t*b
        swap(a,b)
        u-=t*v
        swap(u,v)
    u%=m
    if(u<0):
        u+=m
    return u



n,m=map(int,input().split())
nagasa=len(str(m))
n=n-nagasa
# d=math.floor(10**n/m)
# a=(math.floor(n/m))%m
# b=(10**n)%m
# c=(a*b)%m
mod=m
a=
a=modpow(10,n,m)
b=a*modinv()
print(modpow(10,n,m))
print(3**4%4)
