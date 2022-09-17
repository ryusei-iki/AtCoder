#全探索
n=int(input())
a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=map(int,input().split())
huku_a=0
min_a=float('inf')
min_b=float('inf')
min_a_2=float('inf')
min_b_2=float('inf')
for i in range(n):
    if(a[i]<=min_a):
        huku=0

        if(a[i]==min_a):
            huku=1
        else:
            min_a_2=min_a
        min_a=a[i]
        min_a_2=min_a
        min_a_num=i
    if(b[i]<=min_b):
        huku=0

        if(b[i]==min_b):
            huku=1
        else:
            min_b_2=min_b
        min_b=b[i]
        min_b_num=i
min_a_2=sorted(a)[-2]
min_b_2=sorted(b)[-2]
if(min_a_num==min_b_num):
    if(huku==1):
        print(max(min_a,min_b))
    else:
        print(min(max(min_a,min_b_2),max(min_b,min_a_2),min_a+min_b))
else:
    print(max(min_a,min_b))
