A,B,H,M=map(int,input().split())
import math
H_k=H*30+M/60*30
M_k=M*6
if(M_k==0):
    M_k=360
if(H_k==0):
    H_k=360

if(H_k-M_k<=180 ):
    x=H_k-M_k

else:
    x=M_k-H_k
x=abs(x)

if(x==90):

    print((A**2+B**2)**0.5)
elif(x==180):
    print(A+B)
else:

    z=((A*(math.sin(math.radians(x))))**2+(B-(A*math.cos(math.radians(x))))**2)**0.5
    #zz=(A**2+B**2-2*B*A*math.cos(math.radians(x)))**0.5
    print(z)
