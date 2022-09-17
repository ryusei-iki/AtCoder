n,D,H=map(int,input().split())

d=[0]*n
h=[0]*n
for i in range(n):
    d[i],h[i]=map(int,input().split())
ans=0
for i in range(n):
    ans=max(ans,H-D*((H-h[i])/(D-d[i])))
    #print(H-((H-h[i])/(D-d[i])))

print(ans)
