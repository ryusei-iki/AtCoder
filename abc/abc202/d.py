#@
a,b,k=map(int,input().split())

import math

ans=''
a_da=0
b_da=0
for i in range(1,a+b):

    if(b-b_da==0):
        ans=ans+'a'
    elif(a-a_da==0):
        ans=ans+'b'
    else:
        saidai=int( math.factorial(a+b-i)/(math.factorial(b-b_da)*(math.factorial(a+b-i-b+b_da)) ) )

        if(k<=saidai):
            ans=ans+'a'
            a_da=a_da+1
        else:
            k=k-saidai
            ans=ans+'b'
            b_da=b_da+1

if(a_da==a):
    ans=ans+'b'
else:
    ans=ans+'a'
print(ans)
