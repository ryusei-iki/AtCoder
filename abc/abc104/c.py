D,G=map(int,input().split())
p=[0]*D
c=[0]*D

for i in range(D):
    p[i],c[i]=map(int,input().split())
min_num=float('inf')
for i in range(1<<D):
    goukei=0
    num=0
    for j in range(D+1):
        if((i>>j) & 1 ==1):
            goukei=goukei+p[j]*100*(j+1)+c[j]
            num=p[j]+num
    if(G<=goukei and num<min_num):
        min=goukei
        min_num=num

print(min_num)
