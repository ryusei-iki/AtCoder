#整数
n=int(input())
nn=n
ans=[]
for n in range(1000000):
    ans=[]
    nn=n
    while(1):
        if(n==0):
            break
        if(int(str(n)[-1])%2==0):
            n=n//2
            ans.append('B')
        else:
            n=n-1
            ans.append('A')


    ans.reverse()

    # print(''.join(ans))
    kari=0
    for i in range(len(ans)):
        if(ans[i]=='A'):
            kari=kari+1
        else:
            kari=kari*2

    # print(kari)
    if(nn==kari):
        pass
    else:
        print('dame')
        print(nn)
        exit()
