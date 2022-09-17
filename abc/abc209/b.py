#@
n,x=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    if((i+1)%2==0):
        x=x-(a[i]-1)
    else:
        x=x-a[i]
    if(x<0):
        print('No')
        exit()
print('Yes')
