
D=int(input())
c=[]
c=list(map(int,input().split()))
s=[]
for i in range(D):
    s.append(list(map(int,input().split())))
ans=[0 for i in range(D)]
for i in range(D):
    mamax=max(s[i])
    ans[i]=s[i].index(mamax)+1
for i in range(D):
    print(ans[i])
print()
