#全探索
#整数
n=int(input())
s=list(map(int,input().split()))
check=[0]*1000
for i in range(1,250+1):
    for j in range(1,250+1):
        if(1000<4*i*j+3*i+3*j):
            break
        else:
            check[4*i*j+3*i+3*j-1]=1
ans=0
for i in range(n):
    if(check[s[i]-1]==1):
        pass
    else:
        ans=ans+1
print(ans)
