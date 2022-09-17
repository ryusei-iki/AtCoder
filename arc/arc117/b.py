n=int(input())
a=list(map(int,input().split()))

a=list(set(a))
a.sort()
ans=1
mae=0

for i in range(len(a)):
    ans=(ans*(a[i]-mae+1))%(10**9+7)
    mae=a[i]
print(ans%(10**9+7))
