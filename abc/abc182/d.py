#全探索
N=int(input())
A=list(map(int,input().split()))
wa=0
def cumsum(xs):
    result = [xs[0]]
    for x in xs[1:]:
        result.append(result[-1] + x)
    return result

d=cumsum(A)

ma=[-float('inf')]*N

waa=0

ma[0]=d[0]
for i in range(1,N):

    ma[i]=max(0,ma[i-1],d[i])

wa=A[0]
mmax=max(0,A[0])
for i in range(1,N):


    aa=max(wa+ma[i-1],wa+d[i])

    wa=d[i]+wa

    if(mmax<aa):
        mmax=aa



print(mmax)
