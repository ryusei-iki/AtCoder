#整数 全探索
import math
x,y,a,b=map(int,input().split())



if(b<=a*x):

    print((y-1-x)//b)
    exit()
else:
    con=0
    if((y-1-x*a)<=0):
        print(con)
        exit()
    con=2
    x=a*x
    while(1):
        x=a*x
        if((y-1-x*a)<=0):

            print(con)
            exit()
        if((b+x)<=x*a):

            print(con+(y-1-x)//b)
            exit()
        con=con+1
