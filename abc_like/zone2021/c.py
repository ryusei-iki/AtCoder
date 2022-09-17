n=int(input())
a=[0]*n
b=[0]*n
c=[0]*n
d=[0]*n
e=[0]*n
for i in range(n):
    a[i],b[i],c[i],d[i],e[i]=map(int,input().split())

dp=[[[0 for i in range(5)] for i in range(3)] for i in range(n+1)]

for i in range(n):
    for j in range(3):
        for k in range(5):
            if(dp[i][j][k]<)
