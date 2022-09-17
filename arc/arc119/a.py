#全探索
import math
n=int(input())
meyasu=int(math.log(n,2))
ans=float('inf')
if(n==1):
    print(1)
    exit()

for i in range(meyasu):
    a=n//(2**(meyasu-i))
    b=meyasu-i
    c=n-(a*2**b)
    if(a+b+c<ans):
        ans=a+b+c
    # print(n/(2**(meyasu-i)),meyasu-i)
    # print(2**(meyasu-i))
print(ans)
