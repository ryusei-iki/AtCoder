#整数
import math
a,b,n=map(int,input().split())

roop=min(n,b-1)

print(math.floor(a*roop/b)-a*math.floor(roop/b))
