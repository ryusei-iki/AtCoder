#@
a,b,c=map(int,input().split())

if(c==0):
    if(b<a):
        print('Takahashi')
    else:
        print('Aoki')
else:
    if(a<b):
        print('Aoki')
    else:
        print('Takahashi')
