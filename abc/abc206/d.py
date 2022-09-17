import sys
sys.setrecursionlimit(20000000)

n=int(input())
a=list(map(int,input().split()))

lis=[[] for i in range(max(a)+1)]
miru=[]
kakunin=[0]*(max(a)+1)

if(n%2!=0):
    kakunin[a[n//2]]=1
for i in range(n//2):
    kakunin[a[i]]=1
    kakunin[a[n - 1 - i]]=1
    if(a[i]==a[n-1-i]):
        pass
    else:
        #lis.append([a[i],a[n-1-i]])
        lis[a[i]].append(a[n-1-i])
        lis[a[n-1-i]].append(a[i])
        miru.append(a[i])
        miru.append(a[n-1-i])
        # lis[a[i]-1]=lis[a[i]-1]+1
        # lis[a[n-1-i] - 1] = lis[a[n-1-i] - 1] + 1
miru=list(set(miru))
# print(lis)
# print(lis)
seen=[False]*(max(a)+1)
nakama=[0]*(max(a)+1)
def dfs(start,dore):
  seen[start]=True
  for i in lis[start]:
    if(seen[i]==False):
      if(nakama[dore]==0):
          #nakama[dore]=nakama[dore]+1
          pass
      seen[i]=True
      nakama[dore]=nakama[dore]+1
      dfs(i,dore)
ans=0
for i in range(len(miru)):
    dfs(miru[i],i)
    ans = nakama[i] + ans

# print(nakama)
print(ans)