
#全探索
n=int(input())
s=[0]*n
t=[0]*n
for i in range(n):
    s[i],t[i]=map(str,input().split())
for i in range(n):
    t[i]=int(t[i])

t_max=max(t)
are=0
for i in range(n):
    if(are<t[i] and t_max!=t[i]):
        are=t[i]
        ans=s[i]
print(ans)
