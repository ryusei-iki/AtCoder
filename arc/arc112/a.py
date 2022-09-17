
t=int(input())
l=[0]*t
r=[0]*t
for i in range(t):
    l[i],r[i]=map(int,input().split())
print(l,r)
print()
for i in range(t):
    saidai=r[i]-l[i]
    if(l[i]<saidai):
        saisyo=l[i]
        end=r[i]-l[i]
        start=l[i]+1
        print(((end-start)*(start+end))/2)
        saisyou=max(l[i],r[i]-l[i]+1)
    else:
        print(0)
