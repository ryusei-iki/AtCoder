#全探索
#組合せ
import math
n=int(input())
a=list(map(int,input().split()))
a.sort()

lis=[0]*200
check=[0]*200
for i in range(n):
    lis[a[i]%200]=lis[a[i]%200]+1


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans=0


for i in range(200):

    if(lis[i]==0 or lis[i]==1):
        pass
    # elif(check[i]==0):
    #     ans=ans+combinations_count(lis[i], 2)
    #     print(ans)
    else:

        ans=ans+combinations_count(lis[i], 2)


print(ans)
