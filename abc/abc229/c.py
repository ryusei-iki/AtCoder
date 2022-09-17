#貪欲法
n,w=map(int,input().split())
ab=[0]*n
b=[0]*n
for i in range(n):
    ab[i]=list(map(int,input().split()))

ab=sorted(ab,reverse=True)
ans=0
omosa=0
for i in range(n):
    if(w<omosa+ab[i][1]):
        koredake=w-omosa
        ans=ans+koredake*ab[i][0]
        break
    else:
        ans=ans+ab[i][0]*ab[i][1]
        omosa=omosa+ab[i][1]
print(ans)
