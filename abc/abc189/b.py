#浮動小数点
from decimal import Decimal
n,x=map(int,input().split())
v=[0]*n
p=[0]*n
for i in range(n):
    v[i],p[i]=map(int,input().split())
wa=Decimal(0)

for i in range(n):
    wa=wa+Decimal(v[i])*Decimal(p[i])/Decimal(100)
    wa=Decimal(wa)

    if(x<wa):
        print(i+1)
        exit()
print(-1)
