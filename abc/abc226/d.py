#gcd
n=int(input())
x=[0]*n
y=[0]*n
for i in range(n):
    x[i],y[i]=map(int,input().split())
from collections import defaultdict
p_exist=defaultdict(int)


ans=(n-1)*(n)

def seihu(x):
    if(0<=x):
        return '+'
    else:
        return '-'
for i in range(n):
    for j in range(n):
        if(i==j):
            pass
        else:
            if(x[j]-x[i]==0):
                if(y[j]<y[i]):
                    if(p_exist['-1']==1):
                        ans=ans-1
                    else:
                        p_exist['-1']=1
                elif(y[i]<y[j]):
                    if(p_exist['-2']==1):
                        ans=ans-1
                    else:
                        p_exist['-2']=1
            elif(y[j]-y[i]==0):
                if(x[j]<x[i]):
                    if(p_exist['-3']==1):
                        ans=ans-1
                    else:
                        p_exist['-3']=1
                elif(x[i]<x[j]):
                    if(p_exist['-4']==1):
                        ans=ans-1
                    else:
                        p_exist['-4']=1
            else:
                kigou=seihu(x[j]-x[i])
                kigou1=seihu(y[j]-y[i])

                if(p_exist[((x[j]-x[i])/(y[j]-y[i]),kigou+kigou1)]):
                    ans=ans-1
                else:
                    p_exist[((x[j]-x[i])/(y[j]-y[i]),kigou+kigou1)]=1
        # print(ans,i)
        # print(p_exist)
    # print(ans,i)
    # print(p_exist)
    # print('[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]')
# print(p_exist)
print(ans)
