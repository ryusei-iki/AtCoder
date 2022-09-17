#sort
h,w,n=map(int,input().split())
a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=map(int,input().split())

yoko=[]
tate=[]

yoko={x:i+1 for i,x in enumerate(sorted(list(set(b))))}
tate={x:i+1 for i,x in enumerate(sorted(list(set(a))))}

for i in range(n):
    print(tate[a[i]],yoko[b[i]])
