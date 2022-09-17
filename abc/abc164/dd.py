S=input()
ss=[ int(S) for i in S]
ss=reversed(ss)
n=len(S)
keta=10000
count=0
da=[[0 for i in range(n-4)] for i in range(n-3)]
da[0][0]=ss[n-1]+ss[n-2]*10+ss[n-3]*100+ss[n-4]*1000
for i in range(n-3):
    for j in range(1,n-4):
        da[i][j]=da[i][j-1]+ss[j]*1000*j
        if(da[i][j]%2019==0):
            count=count+1


print(count)
