a=[]
for i in range(10):
    a.append(input())
for i in range(10):
    for j in range(10):
        if(a[i][j]!='o'):
            dfs(i,j,100)
print(a[0][0])


def dfs(i,j,nokori):
    if(dfs(i-1,j,nokori-1)==1):

    elif(dfs(i-1,j,nokori-1)==0)
