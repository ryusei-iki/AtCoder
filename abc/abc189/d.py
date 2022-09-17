#全探索
n=int(input())
s=[0]*n
for i in range(n):
    s[i]=input()


lis=[0]*n
lis[0]=True
tur=[0]*(n+1)
tur[0]=1
for i in range(n):
    if(s[i]=='AND'):
        tur[i+1]=tur[i]
    else:
        tur[i+1]=tur[i]+2**(i+1)
print(tur[-1])
