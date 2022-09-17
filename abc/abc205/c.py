#@
a,b,c=map(int,input().split())
 
if(c%2==0):
    if(abs(a)<abs(b)):
        print('<')
    elif(abs(b)<abs(a)):
        print('>')
    else:
        print('=')
else:
    if(a<b):
        print('<')
    elif(b<a):
        print('>')
    else:
        print('=')