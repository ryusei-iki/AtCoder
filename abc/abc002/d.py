N,M=map(int,input().split())
x=[0]*M
y=[0]*M
friend=[[0 for i in range(N)] for j in range(N)]
for i in range(M):
    x[i],y[i]=map(int,input().split())
    friend[x[i]-1][y[i]-1]=1
    friend[y[i]-1][x[i]-1]=1
box=[]
ans=0
for i in range(1<<N):
    box=[]
    flag=1
    for j in range(N):
        if((i>>j)&1==1):
            box.append(j)

    for k in range(len(box)):
        for o in range(k+1,len(box)):
            if(friend[box[k]-1][box[o]-1]==0):
                flag=0
                break
        if(flag==0):
            break

    if(flag==1):
        ans=max(ans,len(box))

print(ans)
