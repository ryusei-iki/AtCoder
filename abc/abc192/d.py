x=input()
m=int(input())

x_str=str(x)
min_m=float('inf')
for i in range(len(x_str)):
    min_m=min(min_m,int(x_str[i]))

for i in range(len(x)):
    if(x[i]!=0):
        saidai_num=x[i]
        break

xx=x[0]
saidai=(m/int(xx))**(1/(len(x)-1))
saidai=int(saidai)+1

ans=0
wa=0
if(min_m+1==saidai+1):
    for k in range(len(x)):
        wa=wa+int(x[k])*(min_m+1)**(len(x)-k-1)
    if(m<wa):
        if(min_m==0):
            ans=ans-1
        print(ans)
        exit()
for i in range(min_m+1,saidai+1):

    wa=0
    for j in range(len(x)):

        wa=wa+int(x[j])*i**(len(x)-j-1)


    if(m<wa):
        if(min_m==0):
            ans=ans-1

        print(ans)
        exit()


    ans=ans+1

print('maji????')
