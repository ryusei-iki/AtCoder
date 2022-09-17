#全探索
n=int(input())
a=[0]*(n-1)
b=[0]*(n-1)
for i in range(n-1):
    a[i],b[i]=map(int,input().split())
kari=[a[0],b[0]]
kari_b=b[i]

for i in range(1,n-1):
    if(a[i] in kari):
        c=kari.index(a[i])
        if(len(kari)==1):
            pass
        else:
            kari.pop(c-1)
        continue
    elif(b[i] in kari):
        c=kari.index(b[i])
        if(len(kari)==1):
            pass
        else:
            kari.pop(c-1)
    else:
        print('No')
        exit()
print('Yes')
