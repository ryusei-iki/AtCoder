#貪欲法
p=int(input())

import math
ima=p
n=10
con=0
while(n!=0):
    if(ima//math.factorial(n)==0):

        n=n-1
    elif(0<ima-ima//math.factorial(n)*math.factorial(n)):

        con=ima//math.factorial(n)+con
        ima=ima-ima//math.factorial(n)*math.factorial(n)

        n=n-1
    elif(0==ima-ima//math.factorial(n)*math.factorial(n)):
        con=ima//math.factorial(n)+con
        ima=ima-ima//math.factorial(n)*math.factorial(n)

        break

print(int(con))
