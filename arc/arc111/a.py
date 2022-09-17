
import math
n,m=map(int,input().split())
a=pow(10,n,m*m)
b=a//m
c=b%m
print(a)
print(b)
print(c)
# print()
# print((math.floor((n/m))%m*((10**n)%m))%m)
# print(math.floor(n/m*10**n)%m)
