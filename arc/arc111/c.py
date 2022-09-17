


def mpower(a, b, n):
    if b==0:
        return 1
    if b==1:
        return a%n
    a1=a
    k=1
    while a1<n and k<b:
        a1=a1*a
        k=k+1

    a1=a1%n
    b1=b//k
    a2=a
    b2=b%k
    return (mpower(a1,b1,n)*mpower(a2,b2,n))%n
import math
n,m=map(int,input().split())

print(mpower(math.floor(10**n/m),1,m))
