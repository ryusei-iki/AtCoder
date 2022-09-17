#@

n=int(input())
a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=map(int,input().split())


wa=0

wa=[0]*n
a_saidai=sum(a)

for i in range(n):
    wa[i]=a[i]*2+b[i]

wa.sort(reverse=True)


wawawa=0
for i in range(n):
    wawawa=wawawa+wa[i]
    if(a_saidai-wawawa<0):
        print(i+1)
        exit()
