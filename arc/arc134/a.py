#ceil
import math
n,l,w=map(int,input().split())
a=list(map(int,input().split()))
mae=0
ans=0

for i in range(n):
    nokori=max(a[i]-mae,0)
    #kazu=math.ceil(nokori/w)
    kazu=-(-nokori//w)
    ans=ans+kazu
    mae=a[i]+w

nokori=max(l-mae,0)
#kazu=math.ceil(nokori/w)
kazu=-(-nokori//w)
ans=ans+kazu

print(ans)
