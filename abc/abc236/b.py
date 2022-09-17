#@
n=int(input())
a=list(map(int,input().split()))
ima=sum(a)
goukei=0
for i in range(1,n+1):
    goukei=goukei+4*i
print(goukei-ima)
