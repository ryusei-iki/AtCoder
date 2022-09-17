#dict
n,k=map(int,input().split())
c=list(map(int,input().split()))
c_set=set(c)
c_sort=sorted(c_set)
d={s:0 for s in c_sort}
ans=0

kari=0
for i in range(k):

    if(d[c[i]]==0):
        d[c[i]]=1
        kari=kari+1
    else:
        d[c[i]]=d[c[i]]+1

    if(ans<kari):
        ans=kari


for i in range(k,n):
    d[c[i-k]]=d[c[i-k]]-1
    if(d[c[i-k]]==0):
        kari=kari-1

    if(d[c[i]]==0):
        d[c[i]]=1
        kari=kari+1
    else:
        d[c[i]]=d[c[i]]+1

    if(ans<kari):
        ans=kari

print(ans)
