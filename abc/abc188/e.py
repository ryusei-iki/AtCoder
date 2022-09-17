import pprint
n,cc=map(int,input().split())

a=[0]*n
b=[0]*n
c=[0]*n
for i in range(n):
    a[i],b[i],c[i]=map(int,input().split())

d=[0]*n
for i in range(n):
    d[i]=[a[i],b[i]+1]

print(d)
# pea=list(pprint.pprint(sorted(d), width=20))
pea=sorted(d)
print(pea)
ans=0
print(pea)
ima=c[0]

for i in range(1,n):
    print(i)
    if(pea[i-1][1]<=pea[i][0]):
        ans=ima*(ima_b-ima_a)
        ima=0
        pass
    else:
        if(cc<ima):
            ans=ans+cc*(pea[i][0]-pea[i-1][0])
        else:
            ans=ans+ima*(pea[i][0]*pea[i-1][0])
        ima=ima-c[[i]]
    if(cc<ima):
        ans=ans+cc*(pea[i][0]-pea[i-1][0])
    else:
        ans=ans+ima*(pea[i][0]*pea[i-1][0])
print(ans)
