#sort
#全探索
import math
n,m=map(int,input().split())
if(m==0):
    print(1)
    exit()
a=list(map(int,input().split()))
a.sort()
mae=0
haba_min=float('inf')
haba=[]
for i in range(m):

    if(a[i]-mae-1!=0):

        haba_min=min(haba_min,a[i]-mae-1)
        haba.append(a[i]-mae-1)
    mae=a[i]
haba.append(n-mae)
ans=0

for i in range(len(haba)):
    ans=math.ceil(haba[i]/haba_min)+ans
print(ans)
