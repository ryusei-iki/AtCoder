#@
n=int(input())
a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=map(int,input().split())

a_time=0
a_zenbu=0
for i in range(n):
    a_time=a[i]/b[i]
    a_zenbu=a_time+a_zenbu

jikan=a_zenbu/2
ans=0

for i in range(n):
    if(jikan-a[i]/b[i]<=0):
        ans=ans+b[i]*jikan
        break
    else:
        jikan=jikan-a[i]/b[i]
        ans=ans+a[i]
print(ans)
