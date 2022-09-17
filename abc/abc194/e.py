
n,m=map(int,input().split())
a=list(map(int,input().split()))

min_a=min(a[0:m])
min_lis=list(set(sorted(a[0:m])))
for i in
con=0

while(1):
    if(len(min_lis)<=con):
        min_a=con
        break
    if(min_lis[con]==con):
        while(1):

        con=con+1
    else:
        min_a=con
        break
ima=[0 for i in range(min_a)]
print(min_a)

for i in range(m,n):
    if(a[i]<min_a):
        min_a=a[i]
print(min_a)
