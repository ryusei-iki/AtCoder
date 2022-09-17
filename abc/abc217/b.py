#@
s=[0]*3
for i in range(3):
    s[i]=input()
moto=['ABC','ARC','AGC','AHC']
moto=set(moto)
s=set(s)
print(list((moto-s))[0])
