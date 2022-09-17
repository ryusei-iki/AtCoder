#@
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x_min=-1*float('inf')
x_max=float('inf')
if(n==1):
    print(b[0]-a[0]+1)
    exit()
for i in range(n):
    x_min=max(x_min,a[i])
    x_max=min(x_max,b[i])

if(x_min<=x_max):
    print(x_max-x_min+1)
else:
    print(0)
