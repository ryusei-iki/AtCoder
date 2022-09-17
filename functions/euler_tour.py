x=list(map(int,input().split()))
edge=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

euler_basyo=[]
euler_atai=[]
euler_basyo.append(1)
euler_atai.append(x[0])
check=[0]*(n+1)
check[1]=1

def dfs(koko):
    for i in range(len(edge[koko])):
        if(check[edge[koko][i]]==0):
            euler_basyo.append(edge[koko][i])
            euler_atai.append(x[edge[koko][i]-1])
            check[edge[koko][i]]=1
            dfs(edge[koko][i])
            euler_basyo.append(-edge[koko][i])
            euler_atai.append(-x[edge[koko][i]-1])
dfs(1)
euler_basyo.append(-1)
euler_atai.append(x[0])
euler_in=[0]*(n+1)
euler_out=[0]*(n+1)

for i in range(len(euler_basyo)):
    if(1<euler_basyo[i]):
        euler_in[euler_basyo[i]]=i
    else:
        euler_out[-euler_basyo[i]]=i
