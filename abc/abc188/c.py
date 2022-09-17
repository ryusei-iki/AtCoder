#全探索
n=int(input())
a=list(map(int,input().split()))

a1=max(a[0:len(a)//2])
for i in range(len(a)):
    if(a[i]==a1):
        a11=i+1
a2=max(a[len(a)//2:len(a)])
for i in range(len(a)//2,len(a)):
    if(a[i]==a2):
        a22=i+1

if(a1<a2):
    print(a11)
else:
    print(a22)
