seen=[0]*n


def dfs(goal,start):
  seen[start]=True
  for i in lis[start]:
    if(seen[i]==False):
      seen[i]=True
      dfs(goal,i)
      