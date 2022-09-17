S=input()

n=len(S)
s_n=[0]*n
for i in range(n):
    s_n[i]=int(S[i])
count=0
keta=10000
a=s_n[0]*1000+s_n[1]*100+s_n[2]*10+s_n[3]
print(n)
lista= [ i for i in range(3,n)]
for i in reversed(lista):

    for j in reversed(range(n-4)):
        print(j)
        if(a%2019==0):
            count=count+1
        a=a+s_n[j-1]*keta
        keta=keta*10
    if(a%2019==0):
        count=count+1
    keta=10000
    a=s_n[i-4]*1000+s_n[i-3]*100+s_n[i-2]*10+s_n[i-1]
print(count)
