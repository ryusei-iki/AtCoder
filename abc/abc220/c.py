#@
n=int(input())
a=list(map(int,input().split()))
x=int(input())
zenbu=sum(a)
meyasu=x//zenbu
goukei=x//zenbu*zenbu
for i in range(n):
    if(x<(goukei+a[i])):
        print(meyasu*n+i+1)
        break
    else:
        goukei=goukei+a[i]
