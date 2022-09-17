#全探索
a,b,w=map(int,input().split())
ans_min=float('inf')
ans_max=-1*float('inf')
for i in range(1,10**6+1):
    if(a*i<= w*1000 and 1000*w <= b*i):
        ans_min=min(ans_min,i)
        ans_max=max(ans_max,i)

if(ans_min==float('inf')):
    print('UNSATISFIABLE')
else:
    print(ans_min,ans_max)
