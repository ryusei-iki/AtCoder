seen=[0]*n

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