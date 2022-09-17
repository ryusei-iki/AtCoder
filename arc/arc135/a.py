#メモ化再帰
x=int(input())
kari=[]
con=0
tugi=x
ans_kari=1

if(x==1 or x==3):
    print(x)
    exit()



dict={}

def kotae(x):
    if(x//2==1):
        dict[x]=x
        return x
    else:
        if(dict.get(x//2)):
            a=dict[x//2]
        else:
            a=kotae(x//2)
        if(dict.get(-(-x//2))):
            b=dict[x//2]
        else:
            b=kotae(-(-x//2))
        dict[x]=(a*b)%(998244353)
        return a*b

kotae(x)

print(dict[x])
