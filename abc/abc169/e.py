import math
import decimal


N=int(input())
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))

a=[]
b=[]

for i in range(N):
    a.append(A[i][0])
    b.append(A[i][1])
a.sort()
b.sort()

if(N%2==0):
    a_mid=(a[N//2-1]+a[N//2])/2
    b_mid=(b[N//2-1]+b[N//2])/2
    '''
    a[N//2-1]=decimal.Decimal(a[N//2-1])
    a[N//2]=decimal.Decimal(a[N//2])
    b[N//2-1]=decimal.Decimal(b[N//2-1])
    b[N//2]=decimal.Decimal(b[N//2])
    a_mid=(a[N//2-1]+a[N//2])/decimal.Decimal(2)
    b_mid=(b[N//2-1]+b[N//2])/decimal.Decimal(2)
    '''
    #a_mid=decimal.Decimal((a[N//2-1]+a[N//2])/2)
    #b_mid=decimal.Decimal((b[N//2-1]+b[N//2])/2)
    if(a_mid-int(a_mid)<0.5):
        a_mid=int(a_mid)+0.5
    elif(0.5<a_mid-int(a_mid)):
        a_mid=math.ceil(a_mid)

    if(b_mid-int(b_mid)<0.5):
        b_mid=int(b_mid)+0.5
    elif(0.5<b_mid-int(b_mid)):
        b_mid=math.ceil(b_mid)



    sa=b_mid-a_mid
    print(int(sa)*2+1)


else:

    a_mid=a[int(N/2)]
    b_mid=b[int(N/2)]



    sa=b_mid-a_mid
    print(int(sa)+1)
