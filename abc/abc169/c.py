import math
import decimal




A,B=map(str,input().split())


a=decimal.Decimal(A)
b=decimal.Decimal(B)

print(int(a*b))

'''
a=int(A)
b=float(B)*100
#print(int(B))

bb=int(b)

print(math.floor(a*bb//100))
'''
