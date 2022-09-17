#@
r,x,y=map(int,input().split())

kyori=(x**2+y**2)**0.5
if(kyori==r):
    print(1)
elif(kyori<r):
    print(2)

elif(kyori%r==0):
    print(int(kyori//r))
else:
    print(int(kyori//r)+1)
