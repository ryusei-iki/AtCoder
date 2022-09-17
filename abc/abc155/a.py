a,b,c=map(int,input().split())


if(a==b and b==c):
    print('No')
    exit()
    pass
elif(a!=b and a!=c and b!=c):
    print('No')
    exit()
    pass
print('Yes')
