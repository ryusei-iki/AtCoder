#確率
#期待値

from decimal import Decimal
n=int(input())
ans=0
for i in range(1,n):
    #ans=n*(1/i)+ans
    ans=ans+1/(1-Decimal(i)/Decimal(n))
print(ans)
