import math
n,a,b=map(int,input().split())


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
ans=1
# for i in range(n):
#      ans=ans*2%(10**9+7)
ans=pow(2,n,10**9+7)
aa=combinations_count(n,a)
bb=combinations_count(n,b)
ans=ans-aa-bb
ans=ans%(10**9+7)
print(ans)
