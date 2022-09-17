#sort
n,k=map(int,input().split())
a=list(map(int,input().split()))

indices=[*range(len(a))]

sorted_indices=sorted(indices,key=lambda i:-a[i])
sorted_num=[a[i] for i in sorted_indices]

l={sorted_num[i]:i for i in range(len(sorted_num))}


ans=0

if(n==k):
    ans=[1]*n
else:
    ans=[k//n for i in range(n)]
    kijyun=k-k//n*n

    for i in range(n):
        if(len(a)-l[a[i]]<=kijyun):
            ans[i]=ans[i]+1

for i in ans:
    print(i)
