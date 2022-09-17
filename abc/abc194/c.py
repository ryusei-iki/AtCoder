#整数

n=int(input())
a=list(map(int,input().split()))
a_rui=[0]*n
a_rui[0]=a[0]**2
a_wa=[0]*n
a_wa[0]=a[0]
ans=0
for i in range(1,n):
    a_rui[i]=a[i]**2+a_rui[i-1]
    a_wa[i]=a[i]+a_wa[i-1]

for i in range(1,n):

    ans=ans+(n-i)*a[-1*i]**2-2*a[-1*i]*(a_wa[-1*i-1])+a_rui[-1*i-1]
print(ans)
