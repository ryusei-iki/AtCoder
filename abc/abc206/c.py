#dict
#全探索
#sort
n=int(input())
a=list(map(int,input().split()))
a=sorted(a)

dict={i:0 for i in a}

for i in a:
    dict[i]=dict[i]+1

ans=0
for i in range(n):
    ans=ans+(n-i-dict[a[i]])
    dict[a[i]]=dict[a[i]]-1
print(ans)


