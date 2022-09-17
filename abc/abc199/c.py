#@
n=int(input())
s=list(input())
q=int(input())
t=[0]*q
a=[0]*q
b=[0]*q
hanten=0
for i in range(q):
    t[i],a[i],b[i]=map(int,input().split())

for i in range(q):
    if(t[i]==1):
        if(a[i]<n and b[i]<n):
            temp=s[a[i]+(n*hanten)-1]
            s[a[i]+(n*hanten)-1]=s[b[i]+(n*hanten)-1]
            s[b[i]+(n*hanten)-1]=temp
        elif(a[i]<n and n<=b[i]):
            temp=s[a[i]+(n*hanten)-1]
            s[a[i]+(n*hanten)-1]=s[b[i]-(n*hanten)-1]
            s[b[i]-(n*hanten)-1]=temp
        elif(n<=a[i] and b[i]<n):
            temp=s[a[i]-(n*hanten)-1]
            s[a[i]-(n*hanten)-1]=s[b[i]+(n*hanten)-1]
            s[b[i]+(n*hanten)-1]=temp
        elif(n<=a[i] and n<=b[i]):
            temp=s[a[i]-(n*hanten)-1]
            s[a[i]-(n*hanten)-1]=s[b[i]-(n*hanten)-1]
            s[b[i]-(n*hanten)-1]=temp
    else:
        if(hanten==0):
            hanten=1
        else:
            hanten=0
if(hanten==0):


    print(''.join(s))
else:
    temp=s[0:n]
    s[0:n]=s[n:]
    s[n:]=temp
    print(''.join(s))
