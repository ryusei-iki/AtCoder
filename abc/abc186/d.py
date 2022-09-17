#sort 累積和

n=int(input())
a=list(map(int,input().split()))


a.sort(reverse=True)
ans=0

for i in range(len(a)):

    ans=a[i]*(n-i-1)-a[i]*(i)+ans
print(ans)
