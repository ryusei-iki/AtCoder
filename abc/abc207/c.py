#全探索
#条件分け
n=int(input())
t=[0]*n
l=[0]*n
r=[0]*n

for i in range(n):
    t[i],l[i],r[i]=map(int,input().split())
    if(t[i]==2 or t[i]==4):
        r[i]=r[i]-0.5
    if(t[i]==3 or t[i]==4):
        l[i]=l[i]+0.5
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        if(l[i]<=l[j] and l[j]<=r[i]):
            ans=ans+1
        elif(l[i]<=r[j] and r[j]<=l[i]):
            ans=ans+1
        elif(l[j]<=l[i] and l[i]<=r[j]):
            ans=ans+1
        elif(l[j]<=r[i] and r[i]<=l[j]):
            ans=ans+1
print(ans)


