#全探索
n,s,d=map(int,input().split())
x=[0]*n
y=[0]*n
for i in range(n):
    x[i],y[i]=map(int,input().split())

for i in range(n):
    if(x[i]<s and d<y[i]):

        print('Yes')
        exit()
print('No')
