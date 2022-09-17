import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N=int(input())
A=[0]*N
A=list(map(int,input().split()))
s=[0 for i in range(N+1)]
s[0]=0
for i in range(1,N+1):
    s[i]=s[i-1]+A[i-1]


ss=s[1:]
maxmax=max(ss)
minmin=min(ss)
goukei=ss.count(0)
print(ss)
for i in range(minmin,maxmax+1):
    n=ss.count(i)

    if(2<=n):
        goukei=goukei+combinations_count(n,2)

print(goukei)
