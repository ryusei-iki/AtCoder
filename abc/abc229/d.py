#尺取り法
s=list(input())
k=int(input())

ruiseki=[0]*(len(s)+1)
for i in range(len(s)):
    if(s[i]=='.'):
        ruiseki[i+1]=ruiseki[i]+1
    else:
        ruiseki[i+1]=ruiseki[i]
n=len(s)
r=0
ans=0

for l in range(len(s)):
    while(r<n and ruiseki[r+1]-ruiseki[l]<=k):
        r=r+1
    ans=max(ans,r-l)


print(ans)
