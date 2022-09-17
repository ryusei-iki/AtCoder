#@
n=int(input())
a=list(map(int,input().split()))
if(n==1):
    print('')
    exit()
ans=[]
lis=[-1 for i in range(n)]
kesu=-1

for i in range(n-1):
    if(a[i]>a[i+1] ):
        kesu=a[i]
        break

for i in range(n):
    if(kesu==a[i]):
        pass
    else:
        ans.append(a[i])


if(ans==a):
    kesu=a[-1]
    ans=[]
    for i in range(n):
        if(kesu==a[i]):
            pass
        else:
            ans.append(a[i])
    print(*ans)
else:
    print(*ans)
