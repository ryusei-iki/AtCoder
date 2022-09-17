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


for i in range(n):
