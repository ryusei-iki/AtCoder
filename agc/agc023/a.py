import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N=int(input())
A=[0]*N
A=list(map(int,input().split()))
s=[0 for i in range(N+1)]
s[0]=0
mmax=0
mmin=0
for i in A:
    if(0<i):
        mmax=mmax+i
    else:
        mmin=mmin+i
box=[0 for i in range(mmin,mmax+1)]
for i in range(1,N+1):
    s[i]=s[i-1]+A[i-1]
    box[s[i]]=box[s[i]]+1




goukei=s.count(0)-1

for i in box[]:


    if(2<=i):
        goukei=goukei+combinations_count(i,2)

print(goukei)
