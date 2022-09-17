n=int(input())
ss=input()
tt=input()
s=[0]*n
t=[0]*n
for i in range(n):
    s[i]=int(ss[i])
    t[i]=int(tt[i])

ans1=[]
ans=[]
if(sum(s)!=sum(t)):
    print(-1)
    exit()
for i in range(n):
    if(s[i]==0):
        ans.append(i+1)
    if(t[i]==0):
        ans1.append(i+1)
ans2=0
for i in range(len(ans)):
    if(ans[i]!=ans1[i]):
        ans2=ans2+1
print(ans2)
