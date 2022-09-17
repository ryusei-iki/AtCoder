#全探索
n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
for i in range(n):
    if(a[i]==x):
        pass
    else:
        ans.append(a[i])
for i in range(len(ans)):
    print(ans[i],end=' ')
