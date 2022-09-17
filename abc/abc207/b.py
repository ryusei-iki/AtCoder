#全探索
#オーダー
import math
a,b,c,d=map(int,input().split())
ans=-1
diff=c*d-b
if(0<diff):
    ans=math.ceil(a/diff)
    ans=(a-1+diff)//diff
print(ans)
# print(max(-1,math.ceil(-a/(b-c*d))))
